def obtener_complemento(base):
    # si base es A, Retorna T
    if base == 'A':
        return 'T'
    # si base es T, Retorna A
    elif base == 'T':
        return 'A'
    # si base es G, Retorna C
    elif base == 'G':
        return 'C'
    # si base es C, Retorna G
    elif base == 'C':
        return 'G'
    # de los contrario retorna que la letra no es una base
    else:
        raise ValueError(base + " No es una base")

def generar_cadena_complementaria(adn):
    # Obteniendo el complento de una cadena de ADN
    resultado = ""
    # recorre adn
    for base in adn:
        # a resultado le adicionamos el complemento de la letra
        resultado += obtener_complemento(base)
    # retornamos el resultado
    return resultado

def calcular_correspondencia(adn1, adn2):
    # Verificando si la base dos es el complemento de la base uno.
    return adn1 == obtener_complemento(adn2)

def corresponden(adn1, adn2):
    # retorna Bool
    pass


def es_cadena_valida(adn):

    # Recorremos lo que nos llegue en ADN
    for base in adn:
        # validamos si con la funcion es_base
        if not es_base(base):
            # si no es base, retorna false
            return False
    # De lo contrario retornamos True
    return True


def es_base(caracter):

    #Retornamos true o false pasa saber si es o no es una base
    return caracter.upper() in "ATCG"


def es_subcadena(adn1, adn2):

    if not es_cadena_valida(adn2):
        raise ValueError('NO NUMEROS')
    if not es_cadena_valida(adn1):
        raise ValueError('NO NUMEROS')
    if adn2 in adn1:
        return True
    elif adn2 not in adn1:
        return False


def reparar_dano(adn, base):

    if int == type(complementaria):
        raise TypeError('LOS NUMEROS NO SON VALIDOS')
    if not es_cadena_valida(complementaria):
        raise TypeError(complementaria + ' NO ES UNA CADENA VALIDA')
    if corresponden(adn, complementaria):
        return "LAS CADENAS CONCUERDAN"
    elif not corresponden(adn, complementaria):
        return generar_cadena_complementaria(adn)


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

