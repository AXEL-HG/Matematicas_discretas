
#Algoritmo MCD recursivo

def MCD_recursivo(a, b):
    #? Caso base: cuando el segundo número llega a 0, encontramos el MCD
    if b == 0: #* Ale y joel
        return a
    #? Paso recursivo: el divisor pasa a ser el dividendo, y el residuo pasa a ser el divisor
    else:

        q = a // b
        r = a % b
        print(f"   →  {a} = {b}({q}) + {r}")
        return MCD_recursivo(b,r)

print("------ Calculadora de MCD (Algoritmo de Euclides) ------")
num1 = int(input("Inserte el primer número (a): \n → "))
num2 = int(input("Inserte el segundo número (b): \n → "))

#? Convertimos a valor absoluto inmediatamente para cumplir la restricción
a_abs = abs(num1)
b_abs = abs(num2) #* Axel y Fernanando

#? Restricción especial: MCD(0,0) no está definido
if a_abs == 0 and b_abs == 0:
    print("El MCD de 0 y 0 no está definido matemáticamente.")
else:
    #? Ordenamos de mayor a menor
    mayor = max(a_abs, b_abs)
    menor = min(a_abs, b_abs)
    
    #? Mandamos a llamar a la función
    resultado = MCD_recursivo(mayor, menor)
    
    print(f"\nEl Máximo Común Divisor de {num1} y {num2} es: {resultado}")