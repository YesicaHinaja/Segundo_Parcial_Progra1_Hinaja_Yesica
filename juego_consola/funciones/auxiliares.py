
import json 
import csv

#---------------------------------------------------------------------------------------
def menu()->str:
    menu = """ 
    1 - Jugar
    2 - Mostrar Ranking
    3 - Salir
    """
    return menu

def encuadrar(texto:str)->str:
    """
    recibe un texto y lo retorna formateado
    
    """
    parte_sup = """╭═════════════════• ೋ•✧๑♡๑✧•ೋ •════════════════╮"""
    parte_inf = """╰═════════════════• ೋ•✧๑♡๑✧•ೋ •════════════════╯"""
    
    texto_encuadrado = (f"{parte_sup} \n {texto} \n{parte_inf}")
    return texto_encuadrado

# ----------------------------------------------------------------------------------------
def pasar_json_a_dict(ruta_archivo)->dict:
    """Pasa un archivo json a formato diccionario
    Args:
        ruta_archivo: ruta del archivo json

    Returns:
        dict: nuevo diccionario
    """
    with open(ruta_archivo, "r", encoding="UTF-8") as archivo_json:
        dict_config = json.load(archivo_json)
    return dict_config

def pedir_validar_opcion (lista:list)->str:
    """_summary_
    Args:
        lista (list): _description_
    Returns:
        str: _description_
    """
    opcion = input("Ingrese una opción: ").strip()
    if not opcion or opcion not in lista:
        print ("opcion incorrecta")
        return pedir_validar_opcion(lista)
    return opcion.capitalize()

