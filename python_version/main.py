import socket
import json
import utils 
from parity import check_parity_bit
from hamming import hamming_receptor
import random

HOST = '127.0.0.1'
PORT = 8080


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

def add_noise_data(binaryValuesListProccesed, chance_of_flipping = 0.01):
    binaryValuesListProccesedPostNoise = []
    is_word_altered = False
    for char in binaryValuesListProccesed:
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
        binaryValuesListProccesedPostNoise, is_word_altered = add_noise_data(data[0]["binaryValuesListProccesed"], chance_of_flipping=0.01)
        print("All messages processed!")

if __name__ == "__main__":
    main()
