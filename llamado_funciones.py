import adn as funciones

print("Esto Te permitira saber el saber el complemento de una cadena de ADN")
cadena_texto = input("Por favor agregue una cadena de ADN con la misma longitud y separadas por ',' (No escriba las comillas): \n")

archivo = open('archivo.txt', 'w')
archivo.write(cadena_texto+"\n")
archivo.close()
adn = open('archivo.txt', 'r')
texto = adn.readlines()
for ln in texto:
    cadenas = ln.strip().split(',')
print(funciones.calcular_correspondencia(cadenas[0], cadenas[1]))


