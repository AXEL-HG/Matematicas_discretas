def exponenciacion_modular(base, exponente, modulo):
    resultado = 1
    #? Por si la base inicial ya es mayor que el módulo
    base = base % modulo 
    
    while exponente > 0:
        #? 1. Miramos el bit actual (si el exponente es impar, su último bit es 1)
        if (exponente % 2) == 1:
            #? Si el bit es 1, multiplicamos el resultado por la base actual
            resultado = (resultado * base) % modulo
            
        #? 2. Desplazamos los bits (dividimos el exponente entre 2)
        exponente = exponente // 2
        
        #? 3. Elevamos la base al cuadrado para el siguiente bit
        base = (base * base) % modulo
        
    return resultado

print("Probando: 3^11 mod 7")
print("Resultado:", exponenciacion_modular(23, 60, 70))