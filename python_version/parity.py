def add_parity_bit(data):
    count = data.count('1')

    if count % 2 == 0:
        data += '0'
    else:
        data += '1'

    return data

def check_parity_bit(data):
    parity_bit = data[-1]
    data = data[:-1]

    count = data.count('1')

    if (count % 2 == 0 and parity_bit == '0') or (count % 2 == 1 and parity_bit == '1'):
        return True
    else:
        return False

""" data = "1011001"
data_with_parity = add_parity_bit(data)
print("Datos con bit de paridad: " + data_with_parity)
print("Verificación de paridad: " + str(check_parity_bit(data_with_parity)))
 """

if __name__ == "__main__":
    print("Verificación de paridad: " + str(check_parity_bit("01011101")))