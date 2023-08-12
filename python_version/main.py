import socket
import json
import utils 
from parity import check_parity_bit
from hamming import hamming_receptor
import random

HOST = '127.0.0.1'
PORT = 8080


def evaluate_transmission_crc(data):

    print(1) 
    pass

def decode_hamming_after_noise(trama, is_altered):
    msg_concat, was_error_detected, was_error_corrected = hamming_receptor(trama)
    pass

def evaluate_transmission_hamming(data, chance_of_flipping_bit = 0.01):
    errores_detectados = 0
    total_errores = 0
    errores_corregidos = 0
    palabras_correctas = 0
    palabras_intactas = 0

    TP, FP, TN, FN = 0, 0, 0, 0 # Para hacer matriz de confusion


    for word_data_recieved in data:
        WordValuesList = word_data_recieved['binaryValuesList']
        WordProccesed = word_data_recieved['binaryValuesListProccesed']
        WordProccesedWithNoise, is_altered = add_noise_word(WordProccesed, chance_of_flipping=chance_of_flipping_bit)
        for char, was_altered in WordProccesedWithNoise:
            decoded_msg, was_error_detected, was_error_corrected = hamming_receptor(char[0])

            if is_altered: # Si hubo ruido en la trama
                if was_error_detected:
                    if was_error_corrected:
                        TP += 1
                    else:
                        FN += 1
                else:
                    FN += 1
            else: 
                if was_error_detected:
                    FP += 1
                else:
                    TN += 1
    # Cálculo de métricas
    try:
        precision = TP / (TP + FP)
    except ZeroDivisionError:
        precision = 0

    try:
        recall = TP / (TP + FN)
    except ZeroDivisionError:
        recall = 0

    try:
        f1_score = 2 * (precision * recall) / (precision + recall)
    except ZeroDivisionError:
        f1_score = 0

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    # Print the confusion matrix
    print("Matriz de confusión para la codificación Hamming:")
    print(f"TP: {TP}, FP: {FP}, TN: {TN}, FN: {FN}")
    print("Métricas para la codificación Hamming:")
    print(f"Precisión: {precision:.2f}, Exhaustividad: {recall:.2f}, Puntaje F1: {f1_score:.2f}, Exactitud: {accuracy:.2f}")


    

    print(1) 


    pass

def add_noise_trama(binary, chance_of_flipping):
    new_binary = ""
    altered = False
    for char in binary:
        if random.random() < chance_of_flipping:
            new_binary += utils.revert_bit(char)
            altered = True
        else:
            new_binary += char

    return new_binary, altered

def add_noise_word(binaryValueListProccesed, chance_of_flipping = 0.01):
    binaryValuesListProccesedPostNoise = []
    is_word_altered = False
    for char in binaryValueListProccesed:
        new_word = []
        is_char_altered = False
        for bit in char:
            new_binary, is_bit_altered = add_noise_trama(bit, chance_of_flipping=chance_of_flipping)
            if is_bit_altered:
                is_char_altered = True
            new_word.append((new_binary, is_bit_altered))
        
        binaryValuesListProccesedPostNoise.append((char, is_char_altered))
        if is_char_altered:
            is_word_altered = True
    
    return binaryValuesListProccesedPostNoise, is_word_altered
    

def receive_full_data(conn, buffer_size=1024):
    chunks = []
    while True:
        chunk = conn.recv(buffer_size)
        if not chunk:
            break
        chunks.append(chunk)
    return b"".join(chunks)

def get_data(s, total_messages):
    data = []
    for i in range(total_messages):
        print(f"Esperando mensaje No.{i+1} ...")
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            full_data = receive_full_data(conn)
            data_obj = json.loads(full_data.decode())

            """ 
            binaryValuesList = data_obj['binaryValuesList']
            binaryValuesListProccesed = data_obj['binaryValuesListProccesed']
            methodName = data_obj['methodName']
            """

            """
            original_string = utils.binary_list_to_string(binaryValuesList)
            print("Cadena original:", original_string)
            """
            conn.sendall(b"Data obtenido con exito!")
            data.append(data_obj)
    
    return data

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        data = get_data(s, 100)
        method = data[0]["methodName"]

        if method == "hamming":
            evaluate_transmission_hamming(data)
        else: # crc
            evaluate_transmission_crc(data)

        print("All messages processed!")

if __name__ == "__main__":
    main()
