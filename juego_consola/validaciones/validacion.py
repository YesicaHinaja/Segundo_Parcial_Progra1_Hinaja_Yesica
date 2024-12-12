def validar_opcion(num_min:int, num_max:int)->int:
    """_summary_ pide una opcion y la valida dentro de un rango y retorna la opcion validada
    Args:
        num_min (int): numero minimo a ingresar
        num_max (int): numero maximo a ingresar
    Returns:
        int: numero validado
    """
    opcion = input(f"Ingrese una opcion entre {num_min} y {num_max}: ")
    if not opcion or not opcion.isdigit() or int(opcion)<num_min or int(opcion)>num_max:
        print ("ERROR, vuelva a intentarlo...")
        return (validar_opcion(num_min, num_max))
    else: return int(opcion)



