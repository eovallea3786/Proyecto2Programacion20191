"""
Desarrollo: Edward
Pruebas: Johan
Documentación: David
"""
def obtener_complemento(base):

    """
    (str) -> str
    'Recibe una letra y retorna su complemento'

    :param base: Un valor de una cadena de ADN
    :return: El complemento de la candena del ADN
    """
    # retorna caracter
    pass

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

    """
    (str) ->  boolean
    'Recibe una cadena de ADN y se retorna el complento de dicha cadena'

    :param adn: Se recibe una cadena
    :return: El complemento de dicha cadena
    """
    pass


def calcular_correspondencia(adn1, adn2):
    """
    (string, string)->number

    Funcion que calcula el porcentaje de correspondencia de una cadena y otra
    :param adn1: La primera cadena que voy a comparar
    :param adn2 La segunda cadena que voy a comprar
    :return: numbre: el porcentaje de acertividad o un mensaje
    """
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
    """
    str -> boolean

    'recibe dos bases y verifica si la una es el complemento de la otra'
    :param adn1: Se introduce primer parametro
    :param adn2: Se introduce segundo parametro
    :return: Se retorna si son complementos o no
    """
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
    (str) -> boolean

    Funcion que valida si la secuencia en la cadena de ADN es valida



    :param adn: La cadena que se ingresa a evaluar
    :return: True si la cadena de ADN es valida, False si no se cumple
    '''

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
    '''
    (str) -> boolean

    Funcion que recibe un caracter y verifica si es base o no

    :param caracter: El caracter que sera validado
    :return: True es base o False no es base
    '''

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
    '''
    (list of str) -> boolean

    Funcion que recibe dos cadenas y valida si una es una subcadena de la otra


    :param adn1: Recibe la cadena 1
    :param adn2: Recibe la cadena 2
    :return: True si es subcadena o False sino es subcadena
    '''

    pass

"""
Desarrollo: David
Pruebas: Edward
Documentación: Johan
"""
def reparar_dano(adn, base):
    '''

    (list of str, list of str) -> str

    Funcion que reemplaza los elementos no correspondientes con una base dada

    :param adn: Recibe el adn que se corregira
    :param base: Recibe la base dada
    :return: Corrige los elementos no correspondientes con la base dada
    '''

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def obtener_secciones(adn, n):
    """
    (list of str, cantidad de datos a partir de la primera)  -> str

    Funcion que recibe una cadena y de acuerdo a n, obtiene la sección a partir del primer dato de la lista

    :param adn: Recibe el adn del cual se obtendra una seccion
    :param n: Recibe la cantidad de caracteres a partir del primero
    :return: Cadena de caracteres con la sección deseada
    """
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def obtener_complementos(lista_adn):
    """
    str -> str

    Funcion que recibe una cadena y se obitenen los complementos a partir de esta

    :param lista_adn: Recibre un adn al cual se le buscaran los complementos
    :return: lista complementaria
    """
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def unir_cadena(lista_adn):
    """
    str

    :param lista_adn: une cadena
    :return: cadena de caracteres
    """
    pass

"""
Desarrollo: Johan
Pruebas: David
Documentación: Edward
"""
def complementar_cadenas(lista_adn):
    """
    str

    :param lista_adn: recibe una cadena
    :return: cadena de caracteres
    """
    pass