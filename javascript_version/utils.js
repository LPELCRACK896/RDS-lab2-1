// Función auxiliar para contar unos
function countOnes(array) {
    let count = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i] == '1') {
            count++;
        }
    }
    return count;
}

// Función auxiliar para validar la trama
function isValidTrama(trama) {
    for (let i = 0; i < trama.length; i++) {
        if (trama[i] !== '0' && trama[i] !== '1') {
            return false;
        }
    }
    return true;
}


function stringToListAndList(input, filtr_func = (item) => item) {
    const binaryValuesList = []
    const binaryValuesListProccesed = []
    
    for (let i = 0; i < input.length; i++) {
        let asciiValue = input.charCodeAt(i);
        
        let binaryValue = asciiValue.toString(2).padStart(8, '0');
        binaryValuesList.push(binaryValue)
        binaryValuesListProccesed.push(filtr_func(binaryValue))
    }
    
    return { binaryValuesList , binaryValuesListProccesed};
}

module.exports = { countOnes, isValidTrama, stringToListAndList }