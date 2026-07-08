numero_binario = input("Por favor inserte el numero binario que desea convertir: \n → ")

#? 1. Verificamos si el usuario puso un signo negativo al inicio
es_negativo = False                       #* Ale y joel
if numero_binario[0] == "-":
    es_negativo = True
    #? ignorarmos el - si es que el numero es negativo
    numero_binario = numero_binario[1:] 

#? Volteamos la cadena
numero_binario_volteado = numero_binario[::-1] 
#? Hacemos un acumulador para ir armando el numero deciamal
decimal_acumulado = 0 

#?Conversion a decimal
for i in range(len(numero_binario_volteado)): #* Fernando y Axel
    #? Convetimos la cadena en numero para tener el valor decimal 
    bit = int(numero_binario_volteado[i])
    
    #? si el numero es 1 entonces aplicamos la potencia correspondiente en i
    if bit == 1:
        decimal_acumulado += 2 ** i  

#? Si el valor era negativo entonces multiplicamos por -1 para tener el valor acumulado
if es_negativo:
    decimal_acumulado = decimal_acumulado * -1

#? Imprimimos el numero deciamal correspondiente
print(f"El número en decimal es: {decimal_acumulado}")