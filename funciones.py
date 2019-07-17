def contains_str(cadena1, cadena2):
    """Comprueba que la primera cadena se encuentra contenida en la segunda
    cadena.
    
    Arguments:
        cadena1 {[str]} -- Cadena a encontrar
        cadena2 {[str]} -- Cadena base
    """

    cad1 = cadena1.lower()
    cad2 = cadena2.lower()

    puntuacion = 0
    puntuacion_max = 0
    idx = 0
    for val in cad2:
        if cad1[idx] is val:
            idx += 1
            if idx is len(cad1)-1:
                return True
        else:
            idx = 0
    
    return False