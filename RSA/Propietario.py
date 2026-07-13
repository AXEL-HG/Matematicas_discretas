def es_primo(numero): #?Comprobamos si los numero que nos va a dar el usuriario son primos o no y se utiliza un cliclo while para que nos de unocasi obligatorio
    if numero < 2:
        return False
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i = i + 1
    return True


def mcd_extendido(a, b):
    if b == 0:
        return a, 1, 0  #?Utilizamos el algoritmo de resolver congruencias para encontrar el inverso multiplicativo de e mod phi, que es d o en el caso del profesor es u
    g, x1, y1 = mcd_extendido(b, a % b) #? recordemos que resuelve e*x + phi*y = mcd(e,phi) por lo tanto da g
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def cuadrados_sucesivos(base, exponente, modulo): #?se ocupa el algoritmo de cuadrados sucesivos para calcular potencias muy grandes con ayuda de hacerlos binarios 
    resultado = 1
    base = base % modulo

    while exponente > 0:
        if (exponente % 2) == 1: #binarios
            resultado = (resultado * base) % modulo

        exponente = exponente // 2
        base = (base * base) % modulo

    return resultado


#?elegir los primos (deben ser primos y n debe ser mayor a 9)
n = 0 #?esto es para que forzemos que el while se ejecute al mens una vez
while n <= 9: #?aqui lo que hacemos  es que seguimos la regla donde el mensaje M debe ser menor a n ,m depende como lo llames
    
    
    p = int(input("Ingresa un primo p: "))

    
    if not es_primo(p): #?Llamamos a la funcionprimo para que compruebe que es primo o no son como los metodos en java que se llaman desde otra clase
        print("p no es primo, intenta de nuevo.")
        continue

    q = int(input("Ingresa un primo q: "))
    if not es_primo(q):
        print("  q no es primo, intenta de nuevo.")
        continue

    n = p * q #?se calcula n que es el producto de los primos

    if n <= 9: #? hacemos que se cumpla la condicion de que n sea mayor a 9 por ejemplo si agarramos 3 y 2 nos da 6 y no cumple la condicion
        print("  n =", n, "es muy chico, necesitas que p*q sea mayor a 9. Intenta de nuevo.")

# calculos de phi
phi = (p - 1) * (q - 1)
print("n =", n)
print("phi =", phi)

e = 2 #? este ciclo lo que hace es que busca un coprimo automatico con m para que no haya necesidad que el usuario busque uno
while mcd_extendido(e, phi)[0] != 1: #? recordemos que vamos a regresear g ,x ,y lo que hace e [0] es que agarre solamente g que es el mcd de (e , phi)
#?entonces si g !=1 quiere decir que no son coprimos por lo que esta mal
    e = e + 1

g, d, y = mcd_extendido(e, phi)
d = d % phi #?el d es la respuesta de la congruencia de ad = 1 mod phi que es el inverso modular
print("e encontrado automaticamente =", e)
print("d =", d)

print("")
print("Dale esto al cliente para que cifre -> e =", e, " n =", n)
print("")

#? recibir el mensaje cifrado (el cliente te lo pasa, tu lo escribes aqui)
entrada = input("Escribe el mensaje cifrado separado por espacios: ")
cifrado = entrada.split() #? esta funcion lo que hace es que convierte los numero que nos dan en una lista de strings es parecido 

#? descifrado (cada numero cifrado corresponde a un digito, los agrupamos de 3 en 3)
digitos = ""
for c in cifrado: #? lo que hace el for en este codigo es que lo que convierte antes en string que es cifrado y lo descifra con cuadrados susecivos 
    m = cuadrados_sucesivos(int(c), d, n) #? estos son los elementos uno por uno que los descifra con cudrados el int c lo convierte de texto a numero
    digitos = digitos + str(m)#? el str lo que hace es que los numeros que teniamos antes en eneteros los vuelve a convrtir a texto

descifrado = "" #?este es un string vacio que ayuda a ir armando el mesaje poco a poco
i = 0 #?simplemente es un contador que  nos dice la posicion del string
while i < len(digitos): #? este es como un .length en java
    codigo = digitos[i:i + 3] #?lo que hace es que va dividir siempre los numeros en bloques de 3 logico respetando la regla que no tiene que ser mayr a m
    descifrado = descifrado + chr(int(codigo)) #? este lo que hace es que los bloques les aigna la letra que les correponde y asi los va pegando por eso l otra i que va guardando la letra anterionr
    i = i + 3

print("Mensaje descifrado:", descifrado)