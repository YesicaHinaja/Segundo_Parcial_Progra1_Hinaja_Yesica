from validaciones import (validar_opcion)
from funciones import (menu, encuadrar, iniciar_juego)
import os

def juego():
    while True:
        encuadre = encuadrar(menu())
        print (encuadre)
        opcion = validar_opcion(1,3)
        match opcion:
            case 1: iniciar_juego()
            case 2: pass
            case 3:
                break