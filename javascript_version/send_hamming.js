const { stringToListAndList } = require('./utils.js');
const readline = require('readline');
const net = require('net');
const { submitHamming } = require('./hamming.js')
const { submitCRC } = require('./parity.js')


const methods = new Map([
  ["hamming", submitHamming],
  ["crc", submitCRC]
]);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Ingrese una cadena de caracteres: ', (answer) => {
    const { binaryValuesList , binaryValuesListProccesed} = stringToListAndList(answer, hammingProcess);
    console.log("Lista binaria:", binaryValuesList);
    console.log("Lista binaria modificada:", binaryValuesListProccesed);

    // Envía la lista a través de un socket a tu red local
    const client = net.createConnection({ port: 8080 }, () => {
        console.log('Conectado al servidor!');
        client.write(JSON.stringify(binaryValuesList));
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
