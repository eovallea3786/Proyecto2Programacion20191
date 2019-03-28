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

def es_cadena_valida(adn):
    '''
    >>> es_cadena_valida('ATATTACGGC')
    True

    >>> es_cadena_valida('FTATTACGGC')
    False

    >>> es_cadena_valida('')
    False


    :param adn:
    :return:
    '''


def es_base(caracter):
    """
    >>> es_base('A')
    True

    >>> es_base('T')
    True

    >>> es_base('')
    False

    :param caracter:
    :return:
    """
    pass


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, base):
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

