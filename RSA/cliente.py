#? --- Algoritmo de Encriptación ---

def encriptar(clave_publica, mensaje_texto):
    
    #? Desempaquetamos la llave que nos pasó el receptor
    m, e = clave_publica
    
    #? Convertimos a ASCII y aplicamos la fórmula b_j ≡ a_j^e (mod m)
    bloques_a = [ord(caracter) for caracter in mensaje_texto]
    mensaje_encriptado = [pow(a_j, e, m) for a_j in bloques_a]
    
    return mensaje_encriptado

#? --- Ejecución del Cliente ---
if __name__ == '__main__':
    print("------------- LADO DEL CLIENTE -------------")
    
    #? 1. Pega aquí EXACTAMENTE la tupla que generó el receptor.py
    clave_publica_del_receptor = (3233, 2533) 
    
    #? 2. El mensaje que deseas enviar
    mensaje = "HolaMundo"
    
    if clave_publica_del_receptor != (0, 0):
        #? 3. Encriptamos
        encriptado = encriptar(clave_publica_del_receptor, mensaje)
        
        print(f"Mensaje original: {mensaje}")
        print(f"→ Copia este arreglo y pégalo en 'mensaje_recibido_del_cliente' del receptor.py:")
        print(encriptado)
    else:
        print("Error: Por favor actualiza 'clave_publica_del_receptor' con los datos que arrojó el receptor.")