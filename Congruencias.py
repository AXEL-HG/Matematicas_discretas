def euclides_extendido(a, b):
    #? Retorna (mcd, x, y) tal que a*x + b*y = mcd
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = euclides_extendido(b % a, a)
        return mcd, y - (b // a) * x, x

print("Bienvenido al solucionador de congruencias (ax ≡ b mod m)")

a = int(input("Por favor deme el valor de A \n → "))
b = int(input("Por favor deme el valor de B \n → "))
m = int(input("Por favor deme el valor de M \n → "))

#? Obtenemos el MCD y los coeficientes mágicos
mcd, x0, y0 = euclides_extendido(a, m)

#? MCD divide a b
if b % mcd != 0:
    print("Lo siento, la congruencia no tiene solución.")
else:
    #? Calculamos la solución principal
    #?? Multiplicamos el coeficiente x0 por (b / mcd) y sacamos el módulo m
    x_particular = (x0 * (b // mcd)) % m
    
    print(f"\n¡Solución encontrada! La congruencia tiene {mcd} solución(es) módulo {m}:")
    
    #? Si el MCD > 1, hay múltiples soluciones válidas. Las generamos todas:
    for i in range(mcd):
        solucion = (x_particular + i * (m // mcd)) % m
        print(f"x_{i} ≡ {solucion} (mod {m})")