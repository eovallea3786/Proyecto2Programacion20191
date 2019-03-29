"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""
def obtener_complemento(base):

    '''
    >>> obtener_complemento('A')
    'T'
    >>> obtener_complemento('G')
    'C'
    >>> obtener_complemento('T')
    'A'
    >>> obtener_complemento('Z')
    Traceback (most recent call last):
     ...
    ValueError: Z no es una base

    :param base:
    :return:
    '''

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def generar_cadena_complementaria(adn):
    '''
    >>> generar_cadena_complementaria('ATGC')
    'TACG'
    >>> generar_cadena_complementaria('GATC')
    'CTAG'
    >>> generar_cadena_complementaria('CA')
    'GT'

    :param adn:
    :return:
    '''

"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""

def calcular_correspondencia(adn1, adn2):
    # retorna num
    '''

    >>> calcular_correspondencia('ATATTACGGC','TATAATGCCG')
    100.0
    >>> calcular_correspondencia('ATATATCGGC','TATAATGCCG')
    80.0
    >>> calcular_correspondencia('ATATATCGGC','CGATTTACGA')
    20.0

    :param adn1:
    :param adn2:
    :return:
    '''

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
"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""
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
    '''
    >>> corresponden('A','T')
    True
    >>> corresponden('G','T')
    False

    :param adn1:
    :param adn2:
    :return:
    '''

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def es_cadena_valida(adn):

    '''
    >>> es_cadena_valida('ATATTACGGC')
    True
    '''
    # Recorremos lo que nos llegue en ADN
    for base in adn:
        # validamos si con la funcion es_base
        if not es_base(base):
            # si no es base, retorna false
            return False
    # De lo contrario retornamos True
    return True

    >>> es_cadena_valida('FTATTACGGC')
    False

    >>> es_cadena_valida('')
    False


    :param adn:
    :return:
    '''

def es_base(caracter):
    #Retornamos true o false pasa saber si es o no es una base
    return caracter.upper() in "ATCG"

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""

def es_base(caracter):
    """
    >>> es_base('A')
    True

    >>> es_base('T')
    True
    
    >>> es_base('G')
    True
    
    >>> es_base('C')
    True
    
    >>> es_base('B')
    False
    
    >>> es_base('')
    Traceback (most recent call last):
     ...
    ValueError: '' La cadena no puede ser vacia
    

    :param caracter:
    :return:

    """

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""
def es_subcadena(adn1, adn2):
    for adn1 in adn2

    pass

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""
def reparar_dano(adn, base):
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def obtener_secciones(adn, n):
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def obtener_complementos(lista_adn):
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def unir_cadena(lista_adn):
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def complementar_cadenas(lista_adn):
    pass

