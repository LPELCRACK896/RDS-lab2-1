function countOnes(array) {
    let count = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i] == 1) {
            count++;
        }
    }
    return count;
}

function submitCRC() {
    const trama = document.getElementById('code1').value;
    const newTrama = countOnes(trama) % 2 === 0 ? '0' + trama : '1' + trama;
    document.getElementById('response1').innerHTML = `<p>Respuesta: ${newTrama}</p>`;
}