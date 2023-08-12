const  { countOnes, isValidTrama } = require("./utils.js")

function parity(m) {
    let r = 1;
    while (m + r + 1 > Math.pow(2, r)) {
        r += 1;
    }
    return r;
}

function positionsBinary(length, zeroCount) {
    const binaries = [];
    for(let i = 1; i <= length; i++) {
        let binary = i.toString(2);
        while(binary.length < zeroCount) {
            binary = '0' + binary;
        }
        binaries.push(binary);
    }
    return binaries;
}

function dOrP(length, trama) {
    const helper = [];
    let tramaIndex = 0;
    let pCount = 0;
    for (let i = 1; i <= length; i++) {
        if (Math.log2(i) % 1 === 0) {
            helper.push(pCount);
            pCount++;
        } else {
            helper.push(trama[tramaIndex]);
            tramaIndex++;
        }
    }
    return helper;
}

function submitHamming(trama) {
    const paridad = parity(trama.length);
    const longitudMensaje = paridad + trama.length;
    const posicionesBinarias = positionsBinary(longitudMensaje, paridad);
    const nuevaTrama = dOrP(longitudMensaje, trama);
    const operaciones = [];
    const tramaFinal = [...nuevaTrama];
    nuevaTrama.forEach((element, index) => {
        if (typeof element === 'number') {
            const operacion = nuevaTrama.map((flement, jndex) => {
                if (typeof flement === 'string') {
                    const elementoBinario = posicionesBinarias[jndex].split('').reverse().join('');
                    return elementoBinario[element] == 1 ? flement : ' ';
                }
                return ' ';
            });
            operacion[index] = countOnes(operacion) % 2 === 0 ? '0' : '1';
            operaciones.push(operacion);
            tramaFinal[index] = operacion[index];
        }
    });
    return tramaFinal.join('');
}

module.exports = { submitHamming };