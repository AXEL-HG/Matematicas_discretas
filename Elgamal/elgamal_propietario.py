import random


def criba_eratostenes(limite):
    #? Regresa la lista de todos los primos <= limite. Se van tachando los
    #? multiplos de cada primo que se encuentra, hasta llegar a 'limite'.
    if limite < 2:
        return []

    es_primo_lista = [True] * (limite + 1)
    es_primo_lista[0] = False
    es_primo_lista[1] = False

    i = 2
    while i * i <= limite:
        if es_primo_lista[i]:
            multiplo = i * i
            while multiplo <= limite:
                es_primo_lista[multiplo] = False
                multiplo = multiplo + i
        i = i + 1

    primos = []
    numero = 2
    while numero <= limite:
        if es_primo_lista[numero]:
            primos.append(numero)
        numero = numero + 1
    return primos


def es_primo(numero):
    #? Comprobamos si 'numero' es primo generando la Criba de Eratostenes
    #? hasta ese numero y viendo si quedo en la lista de primos.
    if numero < 2:
        return False
    primos = criba_eratostenes(numero)
    return numero in primos


def factorizar(numero):
    #? Separa 'numero' en sus factores primos (division de prueba). Esto se
    #? usa nada mas para poder buscar la raiz primitiva de p.
    factores = []
    d = 2
    m = numero
    while d * d <= m:
        while m % d == 0:
            if d not in factores:
                factores.append(d)
            m = m // d
        d = d + 1
    if m > 1 and m not in factores:
        factores.append(m)
    return factores


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


def raiz_primitiva(p):
    #? Busca automaticamente un 'alpha' que sea raiz primitiva de p, para que
    #? el usuario no tenga que calcularla a mano (igual que buscamos 'e' solo
    #? en RSA). Un alpha es raiz primitiva si, para cada factor primo q de
    #? p-1, se cumple que alpha^((p-1)/q) NO da 1 (mod p).
    factores_p_menos_1 = factorizar(p - 1)
    alpha = 2
    while alpha < p:
        es_raiz = True
        for q in factores_p_menos_1:
            if cuadrados_sucesivos(alpha, (p - 1) // q, p) == 1:
                es_raiz = False
                break
        if es_raiz:
            return alpha
        alpha = alpha + 1
    return None


#?elegir el primo p (parte de la clave publica). Tiene que ser mayor a 122,
#?que es el codigo ASCII de 'z', la letra mas alta que vamos a cifrar
p = 0
while p <= 122:
    p = int(input("Ingresa un numero primo p (mayor a 122): "))

    if not es_primo(p):
        print("  p no es primo, intenta de nuevo.")
        p = 0
        continue

    if p <= 122:
        print("  p =", p, "es muy chico, necesitas que p sea mayor a 122. Intenta de nuevo.")

#?con p ya fijo, buscamos alpha (raiz primitiva) y escogemos e al azar
alpha = raiz_primitiva(p)
e = random.randint(2, p - 2)  #?exponente secreto, esto NUNCA se comparte
a = cuadrados_sucesivos(alpha, e, p)  #?a = alpha^e mod p

print("")
print("p =", p)
print("alpha =", alpha)
print("a =", a)
print("")
print("Dale esto al cliente para que cifre -> p =", p, " alpha =", alpha, " a =", a)
print("(Tu exponente secreto e =", e, " NO se lo des a nadie)")
print("")

#?recibir el mensaje cifrado (el cliente te lo pasa, tu lo escribes aqui)
gamma = int(input("Escribe gamma: "))
entrada = input("Escribe los bloques del mensaje cifrado separados por espacios: ")
bloques = entrada.split()

#?gamma^(-e) = gamma^(p-1-e) (mod p), gracias al pequeño teorema de Fermat
#?(por eso aqui NO hace falta el algoritmo de Euclides extendido, como si
#?se necesito en RSA para encontrar d)
gamma_inv_e = cuadrados_sucesivos(gamma, p - 1 - e, p)

#?descifrado: cada bloque es un numero beta cifrado, o una letra "L" seguida
#?del caracter que viajo sin cifrar (numeros, signos, etc.)
descifrado = ""
for bloque in bloques:
    if bloque[0] == "L":
        descifrado = descifrado + bloque[1:]
    else:
        beta = int(bloque)
        b = (gamma_inv_e * beta) % p  #?recupera el codigo ASCII original
        descifrado = descifrado + chr(b)

print("Mensaje descifrado:", descifrado)
