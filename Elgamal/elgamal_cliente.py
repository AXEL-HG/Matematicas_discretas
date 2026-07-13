import random


def cuadrados_sucesivos(base, exponente, modulo):
    #?se ocupa el algoritmo de cuadrados sucesivos para calcular potencias muy
    #?grandes con ayuda de hacerlos binarios (igual que en nuestro RSA)
    resultado = 1
    base = base % modulo

    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo

        exponente = exponente // 2
        base = (base * base) % modulo

    return resultado


def es_letra(c):
    #?solo ciframos mayusculas, minusculas y el espacio; todo lo demas
    #?(numeros, signos de puntuacion, etc.) viaja sin cifrar
    return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or c == ' '


p = int(input("Ingresa p (clave publica): "))
alpha = int(input("Ingresa alpha (clave publica): "))
a = int(input("Ingresa a (clave publica): "))

mensaje = input("Escribe el mensaje a cifrar: ")

#!IMPORTANTE: antes usabamos un solo k (y un solo gamma) para TODO el
#!mensaje. El problema es que, si la letra se repite, siempre da el mismo
#!numero cifrado (por ejemplo la "a" siempre salia como el mismo beta), y
#!eso deja ver patrones del mensaje aunque este cifrado. Por eso ahora se
#!escoge un k nuevo para CADA letra, asi la misma letra repetida da un
#!numero cifrado distinto cada vez.
bloques = []
for letra in mensaje:
    if es_letra(letra):
        k = random.randint(1, p - 2)  #?numero aleatorio secreto, distinto para cada letra
        gamma = cuadrados_sucesivos(alpha, k, p)  #?gamma = alpha^k mod p
        a_k = cuadrados_sucesivos(a, k, p)  #?a^k mod p

        b = ord(letra)  #?el bloque es directamente el codigo ASCII de la letra o el espacio
        beta = (a_k * b) % p

        bloques.append(str(gamma) + "," + str(beta))
    else:
        bloques.append("L" + letra)  #?caracter que no es letra ni espacio, viaja sin cifrar

texto = ""
for bloque in bloques:
    texto = texto + bloque + " "

print("")
print("Mensaje cifrado, dale esto al propietario:")
print(texto)
