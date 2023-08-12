# Funciones para trabajar con bits de paridad

def add_parity_bit(data: str) -> str:
    """Añade un bit de paridad a la data."""
    count = data.count('1')
    if count % 2 == 0:
        data += '0'
    else:
        data += '1'
    return data

def check_parity_bit(data: str) -> bool:
    """Verifica si el bit de paridad es correcto."""
    parity_bit = data[-1]
    data = data[:-1]
    count = data.count('1')
    return data, (count % 2 == 0 and parity_bit == '0') or (count % 2 == 1 and parity_bit == '1')

if __name__ == "__main__":
    # Esto es solo un ejemplo de prueba, puedes expandirlo según tus necesidades
    data_with_parity = add_parity_bit("1011001")
    print("Datos con bit de paridad:", data_with_parity)
    print("Verificación de paridad:", check_parity_bit(data_with_parity))
