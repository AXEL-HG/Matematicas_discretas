#?Algoritmo de la division

print("------ Bienvenido al divisor de numeros ------")

#?Solicitamos al usuario los numeros para proceder con la ejecucion del programa
dividendo = int(input("Por favor inserte el dividendo: \n → "))
divisor = int(input("Por favor inserte el divisor: \n → "))

if (divisor == 0): #? Validamos que el divisor no sea 0
    print ("Lo siento no se puede dividir por 0")
else: 
    cociente = dividendo // divisor #? Calculamos la funcion piso para el cociente entero (q)
    residuo = dividendo % divisor #? Obtenemos el residuo unico donde 0 <= r < divisor

    print(f"Ingreso la expresion {dividendo} / {divisor}")
    print(f"La forma es {dividendo} = {divisor} (q) + r \n donde q es {cociente} y \ r = {residuo} \n por lo tanto se tiene:")
    print(f"{dividendo} = {divisor}({cociente}) + {residuo}")