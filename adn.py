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
        raise ValueError(base + " no es una base")

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
    # retorna Bool
    # Verificando si la base dos es el complemento de la base uno.
    return adn1 == obtener_complemento(adn2)


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

    if adn2 in adn1:
        return True
    else:
        return False


def reparar_dano(adn, base):

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
    complemento = []
    for cadena in lista_adn:
        complemento.append(generar_cadena_complementaria(cadena))
    return complemento


def unir_cadena(lista_adn):
    cadena = ""
    for cadenas in lista_adn:
        for caracter in cadenas:
            cadena = cadena + caracter
    return cadena


def complementar_cadenas(lista_adn):
    lista_complemento = ''

    for complemento in lista_adn:
        lista_complemento += generar_cadena_complementaria(complemento)
    return lista_complemento


