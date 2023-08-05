from simulation_trama_actions import interfer_and_modify_trama
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
    return error_pos

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
    transmitted_message = hamm_transmitter("0101001")


    error_position = hamn_receptor((transmitted_message))
    if error_position == 0:
        print("No se encontraron errores. Trama recibida:", transmitted_message)
    else:
        print(f"Se encontraron errores, la trama se descarta. Posición del error: {error_position}")
