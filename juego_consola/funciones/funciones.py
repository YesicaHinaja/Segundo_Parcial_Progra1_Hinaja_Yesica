from .jugadores import obtener_opcion_jugador, obtener_opcion_jugadores

def iniciar_juego():
    lista_jugador = obtener_opcion_jugador()
    lista_jugadores = obtener_opcion_jugadores()

    for jugador in lista_jugadores:
        respuestas = jugador[1]

        #lista_opcion = jugador[1]
        #for opcion in lista_opcion:
            #print(opcion)
        #print (jugador)
    
    #print (lista_jugador)
    #print (lista_jugadores)