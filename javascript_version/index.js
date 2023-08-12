const { stringToListAndList } = require('./utils.js');
const { submitHamming } = require('./hamming.js')
const { submitCRC } = require('./parity.js')
const randomstring = require('randomstring');
const readline = require('readline');
const net = require('net');


const methods = new Map([
  ["hamming", submitHamming],
  ["crc", submitCRC]
]);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Obtener el método desde los argumentos pasados al script
const methodName = process.argv[2];  // El primer argumento es "node", el segundo es el nombre del script y el tercer argumento es tu primer parámetro real.
const MAX_RETRIES = 5; // You can adjust this number

async function connectAndSend(data) {
    let retries = 0;
    while (retries < MAX_RETRIES) {
        try {
            const client = await new Promise((resolve, reject) => {
                const client = net.createConnection({ port: 8080 }, () => {
                    console.log('Conectado al servidor!');
                    resolve(client);
                });

                client.on('error', (err) => {
                    reject(err);
                });
            });

            client.write(JSON.stringify(data));
            client.end();

            client.on('data', (data) => {
                console.log(data.toString());
            });

            client.on('end', () => {
                console.log('Desconectado del servidor');
            });

            break;  // If successful, break out of the retry loop
        } catch (err) {
            retries++;
            console.error(`Failed to connect. Attempt ${retries} of ${MAX_RETRIES}`);
        }
    }
}

const send_multiple_strings = async (message_size, total_messages) => {
    for (let i = 0; i < total_messages; i++) {
        const message = randomstring.generate({ length: message_size, charset: 'alphanumeric' });
        console.log(`Mensaje ${i}: ${message}`)
        const { binaryValuesList, binaryValuesListProccesed } = stringToListAndList(message, selectedMethod);
        await connectAndSend({binaryValuesList, binaryValuesListProccesed, methodName});
    }
};


if (!methods.has(methodName)) {
    console.error(`El método ${methodName} no es válido.`);
    process.exit(1);
}

const selectedMethod = methods.get(methodName);

const manual_send = () => {
    rl.question('Ingrese una cadena de caracteres: ', (answer) => {
        const { binaryValuesList, binaryValuesListProccesed } = stringToListAndList(answer, selectedMethod);
        console.log("Lista binaria:", binaryValuesList);
        console.log("Lista binaria modificada:", binaryValuesListProccesed);
    
        // Envía la lista a través de un socket a tu red local
        const client = net.createConnection({ port: 8080 }, () => {
            console.log('Conectado al servidor!');
            client.write(JSON.stringify({binaryValuesList, binaryValuesListProccesed, methodName}));
            client.end();
        });
    
        client.on('data', (data) => {
            console.log(data.toString());
            client.end();
        });
        
        client.on('end', () => {
            console.log('Desconectado del servidor');
            rl.close();
        });
    });
}

send_multiple_strings(5, 100)