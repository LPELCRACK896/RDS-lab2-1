def calculate_p(i):
    p = 0
    while (2 ** p) < (p + i + 1):
        p += 1
    return p

def revert_bit(bit: str):
    return '1' if bit == '0' else '0'

def hamn_receptor(msg_concat):
    p = calculate_p(len(msg_concat))
    error_pos = 0
    for i in range(p):
        parity_bit = 0
        for j in range(1, len(msg_concat) + 1):
            if j & (2**i) != 0:
                parity_bit ^= int(msg_concat[j - 1])
        error_pos += (2**i) * parity_bit

    if error_pos > 0 and error_pos <= len(msg_concat):
        # Hay un error, invertir el bit en la posición del error
        msg_concat = list(msg_concat)
        msg_concat[error_pos - 1] = revert_bit(msg_concat[error_pos - 1])
        msg_concat = "".join(msg_concat)
    elif error_pos > len(msg_concat):
        return error_pos, "Error detectado pero no se puede corregir"
    return error_pos, msg_concat

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
            if j & (2**i) != 0:
                parity_bit ^= int(msg_concat[j - 1])
        msg_concat[2**i - 1] = str(parity_bit)
    msg_concat = "".join(msg_concat)
    print("Código de Hamming para el mensaje dado es:", msg_concat)
    return msg_concat

if __name__ == "__main__":

    error_position, received_message = hamn_receptor("111111111111111")
    if error_position == 0:
        print("No se encontraron errores. Trama recibida:", received_message)
    elif received_message == "Error detectado pero no se puede corregir":
        print(f"Se encontró un error, pero no se pudo corregir. Trama recibida: {received_message}")
    else:
        print(f"Se encontró un error y se corrigió. Trama recibida:", received_message)
