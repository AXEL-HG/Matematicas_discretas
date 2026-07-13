def cuadrados_sucesivos(base, exponente, modulo):
    resultado = 1
    base = base % modulo

    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % modulo

        exponente = exponente // 2
        base = (base * base) % modulo

    return resultado


e = int(input("Ingresa e (clave publica): "))
n = int(input("Ingresa n (clave publica): "))

mensaje = input("Escribe el mensaje a cifrar: ")


digitos = ""
for letra in mensaje:
    codigo = str(ord(letra)).zfill(3)
    digitos = digitos + codigo

cifrado = []
for d in digitos:
    m = int(d)
    c = cuadrados_sucesivos(m, e, n)
    cifrado.append(c)

texto = ""
for c in cifrado:
    texto = texto + str(c) + " "

print("")
print("Mensaje cifrado, dale esto al propietario:")
print(texto)