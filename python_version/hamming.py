def calculate_p(i):
    p = 0
    while (2 ** p) < (p + i + 1):
        p += 1
    return p

def revert_bit(bit:str):
    return '1' if bit == '0' else '0'

def interfer_and_modify_trama(concat_trama: str, positions:list):
    error_trama = list(concat_trama)
    for pos in positions:
        if 0<pos<len(concat_trama):
            error_trama[pos] = revert_bit(concat_trama[pos])
    return "".join(error_trama)

def hamm_receptor(msg_concat):
    p = calculate_p(len(msg_concat))
    err_pos = 0
    for i in range(p):
        parity_bit = 0
        for j in range(1, len(msg_concat) + 1):
            if j & (2**i) == (2**i):
                parity_bit ^= int(msg_concat[-j])
        err_pos += (2**i) * parity_bit
    if err_pos == 0:
        return "No se encontraron errores. Trama recibida: " + msg_concat
    else:
        return f"Se encontraron errores, la trama se descarta. Posición del error: {err_pos}"

def hamm_transmitter(msg):
    p = calculate_p(len(msg))
    msg_concat = list('0' * (p + len(msg)))
    j = 0
    k = 0
    for i in range(1, len(msg_concat) + 1):
        if i == 2**j:
            j += 1
        else:
            msg_concat[i - 1] = msg[k]
            k += 1
    for i in range(p):
        parity_bit = 0
        for j in range(1, len(msg_concat) + 1):
            if j & (2**i) == (2**i):
                parity_bit ^= int(msg_concat[-j])
        msg_concat[2**i - 1] = str(parity_bit)
    msg_concat = "".join(msg_concat)
    print("Código de Hamming para el mensaje dado es:", msg_concat)
    return msg_concat

# Tests

def tests():
    # Pruebas

    # Se pasan tres tramas distintas por el emisor. 
    no_error_trama1 = hamm_transmitter("1101")
    no_error_trama2 = hamm_transmitter("1010")
    no_error_trama3 = hamm_transmitter("1001")

    # Introduce un error en cada trama
    one_error_trama1 = list(no_error_trama1)
    one_error_trama1[1] = revert_bit(one_error_trama1[1]) # Cambia el segundo bit
    one_error_trama1 = "".join(one_error_trama1)

    one_error_trama2 = list(no_error_trama2)
    one_error_trama2[2] = revert_bit(one_error_trama2[2])  # Cambia el tercer bit
    one_error_trama2 = "".join(one_error_trama2)

    one_error_trama3 = list(no_error_trama3)
    one_error_trama3[3] = '1' if one_error_trama3[3] == '0' else '0'  # Cambia el cuarto bit
    one_error_trama3 = "".join(one_error_trama3)

    # Introduce dos errores en cada trama
    two_errors_trama1 = list(one_error_trama1)
    two_errors_trama1[4] = '1' if two_errors_trama1[4] == '0' else '0'  # Cambia el quinto bit
    two_errors_trama1 = "".join(two_errors_trama1)

    two_errors_trama2 = list(one_error_trama2)
    two_errors_trama2[5] = '1' if two_errors_trama2[5] == '0' else '0'  # Cambia el sexto bit
    two_errors_trama2 = "".join(two_errors_trama2)

    two_errors_trama3 = list(one_error_trama3)
    two_errors_trama3[6] = '1' if two_errors_trama3[6] == '0' else '0'  # Cambia el séptimo bit
    two_errors_trama3 = "".join(two_errors_trama3)

    # Trama modificada especialmente para que el algoritmo no detecte errores
    # Se selecciona la trama1 y se cambian los dos bits de paridad
    undetectable_error_trama = list(no_error_trama1)
    undetectable_error_trama[0] = '1' if undetectable_error_trama[0] == '0' else '0'  # Cambia el primer bit (bit de paridad)
    undetectable_error_trama[2] = '1' if undetectable_error_trama[2] == '0' else '0'  # Cambia el tercer bit (bit de paridad)
    undetectable_error_trama = "".join(undetectable_error_trama)

    # Pasamos las tramas al receptor
    no_error_msg1 = hamm_receptor(no_error_trama1)
    no_error_msg2 = hamm_receptor(no_error_trama2)
    no_error_msg3 = hamm_receptor(no_error_trama3)

    one_error_msg1 = hamm_receptor(one_error_trama1)
    one_error_msg2 = hamm_receptor(one_error_trama2)
    one_error_msg3 = hamm_receptor(one_error_trama3)

    two_errors_msg1 = hamm_receptor(two_errors_trama1)
    two_errors_msg2 = hamm_receptor(two_errors_trama2)
    two_errors_msg3 = hamm_receptor(two_errors_trama3)

    undetectable_error_msg = hamm_receptor(undetectable_error_trama)

    no_error_trama1, no_error_msg1, one_error_trama1, one_error_msg1, two_errors_trama1, two_errors_msg1, undetectable_error_trama, undetectable_error_msg, no_error_trama2, no_error_msg2, one_error_trama2, one_error_msg2, two_errors_trama2, two_errors_msg2, no_error_trama3, no_error_msg3, one_error_trama3, one_error_msg3, two_errors_trama3, two_errors_msg3


if __name__ == "__main__":
    hamming_code = hamm_transmitter("1101")
    # Introduce dos errores en el código de Hamming
    erroneous_code = list(hamming_code)
    erroneous_code[1] = '1' if erroneous_code[1] == '0' else '0'  # Cambia el segundo bit
    erroneous_code[4] = '1' if erroneous_code[4] == '0' else '0'  # Cambia el quinto bit
    erroneous_code = "".join(erroneous_code)
    print("Código erróneo:", erroneous_code)
    hamm_receptor(erroneous_code)
