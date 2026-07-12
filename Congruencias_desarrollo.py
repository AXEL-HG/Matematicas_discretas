def euclides_extendido_pasos(a, b):
    #? Retorna (mcd, x, y) tal que a*x + b*y = mcd
    if a == 0:
        print(f"\n--- LLEGAMOS AL CASO BASE ---")
        print(f"a = 0, entonces el MCD es {b}")
        print(f"Ecuación base: {a}*(0) + {b}*(1) = {b}\n")
        print(f"--- INICIANDO SUSTITUCIÓN HACIA ATRÁS ---")
        return b, 0, 1
    else:
        # Calculamos cociente y residuo para imprimir el paso
        cociente = b // a
        residuo = b % a
        print(f"División: {b} = {a} * {cociente} + {residuo}")
        
        mcd, x_prev, y_prev = euclides_extendido_pasos(residuo, a)  #* Axel y joel
        
        # Calculamos x e y actuales
        x_actual = y_prev - cociente * x_prev
        y_actual = x_prev
        
        print(f"Sustitución con a={a}, b={b}:")
        print(f"-> {a}*({x_actual}) + {b}*({y_actual}) = {mcd}")
        
        return mcd, x_actual, y_actual


print("Bienvenido al solucionador de congruencias (ax ≡ b mod m)")

a = int(input("Por favor deme el valor de A \n → "))
b = int(input("Por favor deme el valor de B \n → "))
m = int(input("Por favor deme el valor de M \n → "))

print(f"\n=== PASO 1: CALCULAR EL MCD({a}, {m}) ===")
#? Obtenemos el MCD y los coeficientes mágicos
mcd, x0, y0 = euclides_extendido_pasos(a, m)


print(f"=== PASO 2: VERIFICAR SOLUCIÓN ===")
print(f"¿El MCD ({mcd}) divide a B ({b})?")

#? MCD divide a b          
if b % mcd != 0: #* Fernando y Ale
    print(f"No. {b} / {mcd} no es entero. El residuo es {b % mcd}.")
    print("Lo siento, la congruencia no tiene solución.")
else:
    factor_b = b // mcd
    print(f"Sí. {b} / {mcd} = {factor_b}. Por lo tanto, hay {mcd} solución(es).\n")
    
    print(f"=== PASO 3: CALCULAR SOLUCIÓN PARTICULAR ===")
    print(f"Fórmula: x_particular = (x0 * (B // MCD)) mod M")
    
    #? Calculamos la solución principal
    #?? Multiplicamos el coeficiente x0 por (b / mcd) y sacamos el módulo m
    multiplicacion = x0 * factor_b
    x_particular = multiplicacion % m
    
    print(f"Sustituyendo: x_particular = ({x0} * {factor_b}) mod {m}")
    print(f"x_particular = {multiplicacion} mod {m} = {x_particular}\n")
    
    print(f"=== PASO 4: GENERAR TODAS LAS SOLUCIONES ===")
    salto = m // mcd
    print(f"El 'salto' entre soluciones es M // MCD = {m} // {mcd} = {salto}")
    print(f"¡Solución encontrada! La congruencia tiene {mcd} solución(es) módulo {m}:")
    
    #? Si el MCD > 1, hay múltiples soluciones válidas. Las generamos todas:
    for i in range(mcd):
        solucion = (x_particular + i * salto) % m
        print(f"Iteración i={i}: x_{i} = ({x_particular} + {i} * {salto}) mod {m}  ==>  x_{i} ≡ {solucion} (mod {m})")