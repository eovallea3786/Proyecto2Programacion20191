import adn as funciones

print("Esto Te permitira saber el saber el complemento de una cadena de ADN")
cadena_texto = input("Por favor agregue una cadena de ADN con la misma longitud y separadas por ',' (No escriba las comillas): \n")

archivo = open('archivo2.txt', 'w')
archivo.write(cadena_texto+"\n")
archivo.close()
adn = open('archivo2.txt', 'r')
texto = adn.readlines()

for i in adn:
    cadenas = i.strip().split(',')
print(funciones.es_cadena_valida(cadena_texto))
print(funciones.obtener_complementos(cadena_texto))