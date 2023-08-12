const  {countOnes, isValidTrama } = require("./utils.js")


function submitCRC(trama) {
    const newTrama = countOnes(trama) % 2 === 0 ? '0' + trama : '1' + trama;
    return newTrama
}

module.exports = {submitCRC}