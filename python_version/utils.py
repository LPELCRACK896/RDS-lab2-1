def count_ones(binary_str):
    """Cuenta los unos en una cadena binaria."""
    return binary_str.count('1')

def is_valid_trama(trama):
    """Valida si la trama contiene sólo ceros y unos."""
    return all(c in ['0', '1'] for c in trama)

def string_to_binary(input_str):
    """Convierte una cadena a su representación binaria y muestra las equivalencias."""
    binary_str = ''

    for char in input_str:
        ascii_value = ord(char)

        binary_value = format(ascii_value, '08b')  
        print(f"{char} = {ascii_value} = {binary_value}")

        binary_str += binary_value

    return binary_str


def binary_list_to_string(binary_list):
    chars = [chr(int(binary, 2)) for binary in binary_list]
    return ''.join(chars)


def revert_bit(bit: str) -> str:
    """Invierte un bit."""
    return '1' if bit == '0' else '0'




if __name__ == "__main__":
    cadena = "Hello"
    representacion_binaria = string_to_binary(cadena)
    print(representacion_binaria) 