from typing import Callable, Any

def check_valid_position(position, iterable):
    
    return 0<=position


def revert_bit(bit:str):
    return '1' if bit == '0' else '0'

def interfer_and_modify_trama(concat_trama: str, positions:list):
    error_trama = list(concat_trama)
    for pos in positions:
        if 0<pos<len(concat_trama):
            error_trama[pos] = revert_bit(concat_trama[pos])
    return "".join(error_trama)


def tst_scheme_detects_no_error_on_successful_trama(trama:str, func_transmitter:Callable[[str], str], func_receptor:Callable[[str], str]):
    concated_trama = func_transmitter(trama)
    no_error_msg = func_receptor(concated_trama)
    return no_error_msg

def tst_scheme_detects_error_on_defective_trama(trama:str, func_transmitter:Callable[[str], Any], func_receptor:Callable[[str], Any], position_err: int = 1):
    if position_err<0 or position_err>=len(trama):
        position_err = 1 # Se pone otro valor en caso se elija alguno que supere el tamanio de la trama 

    concated_trama = func_transmitter(trama)
    error_concated_trama = interfer_and_modify_trama(concated_trama, [position_err]) # Error en la segunda posicion
    error_msg = func_receptor(error_concated_trama)
    return error_msg

def tst_scheme_not_detects_error_on_defective_trama(trama:str, func_transmitter:Callable[[str], Any], func_receptor:Callable[[str], Any], first_position_err: int = 0, second_position_err: int = 2):
    pass

