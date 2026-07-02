#?Ocupamos el algoritmo de la divicion con 2 para obtener el cociente que va a seguir armando el numero binario
def conversion_binario(dividendo):

    dividendo = abs(dividendo)
    cociente = dividendo // 2
    residuo = dividendo % 2 #?Aplicamos el modulo 2 para obtener el residuo de la divicion ya que solo tendremos los valores 0 o 1

    if cociente == 0: #? Si el cociente es 0 entonces termninamos por lo tanto regreseamos el arreglo
        return [residuo]
    else:
        #? Usamos la recursividad para ir haciendo el array de los binarios
        return conversion_binario(cociente) + [residuo]

print("------------- Bienvenido al conversor de decimal a binario ----------------------")
numero = int(input("Por favor inserte el numero decimal que quiere convertir a binario: \n → "))

array_binario = conversion_binario(numero) #? llamamos a la funcion

print(f"El número {numero} en binario es: ", end="") #?Imprimimos el arreglo

#? Si el numero es negativo imprimimos un - antes
if numero < 0:
    print("-", end="")

for bit in array_binario: #? imprimimios el arreglo
    print(bit, end="") 

print() #?Limpiamos espacio