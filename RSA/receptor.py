import random
import math

def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = euclides_extendido(b % a, a)
        return gcd, y - (b // a) * x, x

def inverso_multiplicativo(e, phi):
    gcd, x, y = euclides_extendido(e, phi)
    if gcd != 1:
        raise Exception("El inverso modular no existe")
    else:
        return x % phi

#? --- Generación y Desencriptación ---

def generar_claves(p, q):
    m = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
        
    u = inverso_multiplicativo(e, phi)
    return ((m, e), (m, u))

def desencriptar(clave_privada, mensaje_encriptado):
    m, u = clave_privada
    bloques_x = [pow(b_j, u, m) for b_j in mensaje_encriptado]
    return "".join([chr(x_j) for x_j in bloques_x])

#? --- Ejecución del Receptor ---
if __name__ == '__main__':
    print("------------- LADO DEL RECEPTOR -------------")
    
    #? 1. Elegimos nuestros números primos
    p = 61
    q = 53
    
    publica, privada = generar_claves(p, q)
    
    #? 2. Mostramos las claves. La pública se la daremos al cliente script.
    print(f"→ Comparte esta Clave Pública al cliente: {publica}")
    print(f"→ Guarda tu Clave Privada en secreto: {privada}\n")
    
    #? 3. Pega aquí el arreglo de números que te devuelva el script del cliente
    mensaje_recibido_del_cliente = [3183, 1941, 1450, 248, 1764, 1120, 2110, 717, 1941]
    
    if mensaje_recibido_del_cliente:
        texto_limpio = desencriptar(privada, mensaje_recibido_del_cliente)
        print(f"Mensaje desencriptado exitosamente: {texto_limpio}")
    else:
        print("Esperando recibir el arreglo encriptado del cliente...")