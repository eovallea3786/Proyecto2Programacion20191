def obtener_complemento(base):
    """
    (str) -> str
    'Recibe una letra y retorna su complemento'
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

    :param base: Un valor de una cadena de ADN
    :return: El complemento de la candena del ADN
    """
    # retorna caracter
    if base == 'A':
        return 'T'
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
        raise ValueError(str(base) + ' no es una base')

def generar_cadena_complementaria(adn):
    """
    (str) ->  str
    'Recibe una cadena de ADN y se retorna el complemento de dicha cadena'
    >>> generar_cadena_complementaria('ATGC')
    'TACG'
    >>> generar_cadena_complementaria('GATC')
    'CTAG'
    >>> generar_cadena_complementaria('CA')
    'GT'

    :param adn: Se recibe una cadena
    :return: El complemento de dicha cadena
    """
    # Obteniendo el complento de una cadena de ADN
    resultado = ""
    # recorre adn
    for base in adn:
        # a resultado le adicionamos el complemento de la letra
        resultado += obtener_complemento(base)
    # retornamos el resultado
    return resultado

def calcular_correspondencia(adn1, adn2):
    # retorna num
    '''
    (str, str)-> number
    Funcion que calcula el porcentaje de correspondencia de una cadena y otra
    >>> calcular_correspondencia('ATATTACGGC','TATAATGCCG')
    100.0
    >>> calcular_correspondencia('ATATATCGGC','TATAATGCCG')
    80.0
    >>> calcular_correspondencia('ATATATCGGC','CGATTTACGA')
    20.0
    >>> calcular_correspondencia('TTGGAACC','ACTA')
    'Las cadenas no tienen la misma longitud'

    :param adn1: La primera cadena que voy a comparar
    :param adn2 La segunda cadena que voy a comparar
    :return: num: el porcentaje de acertividad o un mensaje
    '''
    # Declaramos desde un principio el valor porcentaje en 0
    porcentaje = 0;
    # Declaramos declaramos una posicion para poder acceder a la cadena dos en la posicion en la que este cadena_1
    posicion = 0;

    # validamos que las cadenas tengan la misma longitud
    if (len(adn1) == len(adn2)):
        # recorremos la cadena uno
        for i in adn1:
            # validamos de que posicion de cadena uno en cadena dos sea base
            if (corresponden(i, adn2[posicion])):
                # si es base, suma una unidad al porcentaje
                porcentaje += 1
            # a lo que termine la validacion, pasa a la siguiente posicion
            posicion += 1
        # retornamos el porcentaje
        return porcentaje * 100 / len(adn1)
    # si las cadenas no tienen la misma longitud, retorna um mensaje informando que no tienen la misma longitud
    return 'Las cadenas no tienen la misma longitud'


def corresponden(adn1, adn2):
    """
    str -> boolean
    'recibe dos bases y verifica si la una es el complemento de la otra'
    >>> corresponden('A','T')
    True
    >>> corresponden('G','T')
    False

    :param adn1: Se introduce primer parametro
    :param adn2: Se introduce segundo parametro
    :return: Se retorna si son complementos o no
    """
    # retorna Bool
    # Verificando si la base dos es el complemento de la base uno.
    return adn1 == obtener_complemento(adn2)

def es_cadena_valida(adn):
    '''
    (str) -> boolean
    Funcion que valida si la secuencia en la cadena de ADN es valida
    >>> es_cadena_valida('FTATTACGGC')
    False
    >>> es_cadena_valida('ATATTACGGC')
    True

    :param adn: La cadena que se ingresa a evaluar
    :return: True si la cadena de ADN es valida, False si no se cumple
    '''
    # Recorremos lo que nos llegue en ADN
    for base in adn:
        # validamos si con la funcion es_base
        if not es_base(base):
            # si no es base, retorna false
            return False
        # De lo contrario retornamos True
    return True

def es_base(caracter):
    '''
    (str) -> boolean
    Funcion que recibe un caracter y verifica si es base o no
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

    :param caracter: El caracter que sera validado
    :return: True es base o False no es base
    '''
    #Retornamos true o false pasa saber si es o no es una base
    return caracter.upper() in "ATCG"

def es_subcadena(adn1, adn2):
    """
    (str, str) -> bool
    Funcion que retorna la subcadena de una cadena
    >>> es_subcadena('ATCTTA', 'ATC')
    True
    >>> es_subcadena('TCGA', 'AAT')
    False

    :param adn1: str Primer Cadena
    :param adn2: str Segunda Cadena
    :return: Retorna la subcadena de la primer cadena
    """
    if adn2 in adn1:
        return True
    else:
        return False

def reparar_dano(adn, complementaria):
    """
    (str, str) -> str
    Obtiene dos cadenas y valida si corresponden sino las corrige
    >>> reparar_dano('ATGPPP', 'C')
    'ATGPPP'
    >>> reparar_dano('ATGCCC', 'G')
    'ATGCCC'

    :param adn: str Cadena principal
    :param complementaria: str Caracter para corregir
    :return: str Cadena corregida
    """

    if not es_base(complementaria):
        Exception("La base ingresada para reparar dano no es una base")
    reparado = ""
    for caracter in adn:
        if es_base(caracter):
            reparado = reparado + caracter
        else:
            reparado = reparado + caracter
    return reparado

def obtener_secciones(adn, n):
    """
    (str, int) -> list of str
    Valida cada seccion de una cadena
    >>> obtener_secciones('atata', 3)
    ['a', 't', 'ata']
    >>> obtener_secciones('ATGCTACAG', 2)
    ['ATGC', 'TACAG']

    :param adn: Cadena de ADN
    :param n: Numero de secciones que se quiere dividir
    :return: Resultado de la cadena por secciones
    """
    if not es_cadena_valida(adn):
        raise TypeError('La cadena no es valida')

    suma_secciones = len(adn) // n
    division_seccion = []

    for secciones in range(n):
        resultado = ""
        cantidad = suma_secciones
        if secciones == n - 1 and len(adn) % n != 0:
            cantidad = suma_secciones + len(adn) % n
        for caracter in range(cantidad):
            base_cadena = secciones * suma_secciones + caracter
            resultado = resultado + adn[base_cadena]
        division_seccion.append(resultado)

    return division_seccion

def obtener_complementos(lista_adn):
    """
    (list of str) -> list of str
    Recibe una lista de adn y devuelve la lista de adn complementario
    >>> obtener_complementos(['AAA', 'CGC', 'AAA'])
    ['TTT', 'GCG', 'TTT']
    >>> obtener_complementos(['AGT', 'GTA', 'AAA'])
    ['TCA', 'CAT', 'TTT']

    :param lista_adn: lista de ADN
    :return: Representa una lista de ADN complementario
    """
    complemento = []
    for cadena in lista_adn:
        complemento.append(generar_cadena_complementaria(cadena))
    return complemento

def unir_cadena(lista_adn):
    """
    (list of str) -> str
    Funcion que une todas las cadenas ingresadas
    >>> unir_cadena(['CGTA', 'ATTA'])
    'CGTAATTA'
    >>> unir_cadena(['GC', 'GCATTT'])
    'GCGCATTT'

    :param lista_adn: Lista de ADN ingresadas
    :return: Union de las cadenas
    """

    cadena = ""
    for cadenas in lista_adn:
        for caracter in cadenas:
            cadena = cadena + caracter
    return cadena

def complementar_cadenas(lista_adn):
    """
    Funcion que complenta las lista de ADN ingresadas
    (list of str) -> str
    >>> complementar_cadenas(['GCC','CGG'])
    'CGGGCC'
    >>> complementar_cadenas(['AT','GTA','CC'])
    'TACATGG'

    :param Lista_adn: Lista de ADN ingresada
    :return: Complementos de la lista ingresada
    """

    lista_complemento = ''

    for complemento in lista_adn:
        lista_complemento += generar_cadena_complementaria(complemento)
    return lista_complemento
