from .auxiliares import pasar_json_a_dict, pedir_validar_opcion, encuadrar
import random

#constantes
ARCH_JUGADORES = "datitos/jugadores_config.json"
ARCH_CFG = 'datitos/config2.json'


def obtener_opcion_jugadores(ruta_jugadores_config = ARCH_JUGADORES)->list[list]:
    """recorre el json de configuracion, lo convierte a diccionario,
        lo recorrer, busca el nombre y la opcion y las guarda en una lista,
        una vez obtenido todos los datos los retorna juntos en una lista.
    Args:
        ruta_jugadores_config (_type_): ruta del archivo de configuracion de jugadores.
    Returns:
        lista: lista de listas con info de cada jugador.
    """
    diccionario_jugadores = pasar_json_a_dict (ruta_jugadores_config)
    lista_dict = diccionario_jugadores.get("jugadores")
    list_players_With_option = []
    for diccionario in lista_dict:
        info_jugador = diccionario
        lista_info = []
        for clave, valor in info_jugador.items():
            lista_opciones = valor['opcion']
            nombre = valor['nombre']
            opcion = random.choice(lista_opciones)
            lista_info = [nombre, opcion]
            list_players_With_option.append(lista_info)
    return list_players_With_option

def obtener_opcion_jugador(ruta_config_juego = ARCH_CFG)->list[list]:
    """recorre el diccionario de preguntas, muestra una por una y pide una opcion al usuario,
    valida y guarda en una lista
    Args:
        ruta_config_juego: ruta de configuracion del juego
    Returns:
        list: lista con las respuestas obtenidas
    """
    diccionario = pasar_json_a_dict(ruta_config_juego)
    lista_dict = diccionario.get("preguntas")
    lista_respuestas_jugador= []
    for diccionario in lista_dict:
        lista_op = []
        pregunta = diccionario["pregunta"]
        print (encuadrar(pregunta))
        respuestas = diccionario["respuestas"]
        opcion = pedir_validar_opcion(respuestas)
        lista_op = [opcion]
        lista_respuestas_jugador.append(lista_op)
    return lista_respuestas_jugador
