"""
Este es el programa de la persona B ("el cliente") 
"""

import secrets

from elgamal_comun import (
    es_letra,
    letra_a_codigo,
    guardar_json,
    leer_json,
)

ARCHIVO_CLAVE_PUBLICA = "clave_publica.json"
ARCHIVO_MENSAJE_CIFRADO = "mensaje_cifrado.json"


def encriptar_mensaje(mensaje, p, alpha, a):

    #? ii. k aleatorio, 1 <= k <= p-2, y gamma = alpha^k (mod p)
    k = secrets.randbelow(p - 2) + 1
    gamma = pow(alpha, k, p)
    a_k = pow(a, k, p)   #? a^k (mod p), se reutiliza para cada bloque

    bloques = []
    for c in mensaje:
        if es_letra(c):
            b = letra_a_codigo(c)          #?bloque b < 52 < p
            beta = (a_k * b) % p            #? beta = a^k * b (mod p)
            bloques.append({"tipo": "cifrado", "beta": beta})
        else:
            #? Se cifran letras mayúsculas, minúsculas y el espacio;
            #? lo demás (dígitos, signos, etc.) viaja sin cifrar.
            bloques.append({"tipo": "literal", "valor": c})

    return {"gamma": gamma, "bloques": bloques}


def main():
    print("=== ElGamal - Cliente (persona B) ===")
    try:
        clave_publica = leer_json(ARCHIVO_CLAVE_PUBLICA)
    except FileNotFoundError:
        print(f"No se encontro '{ARCHIVO_CLAVE_PUBLICA}'.")
        print("Pide al propietario que genere y comparta su clave publica.")
        return

    p = clave_publica["p"]
    alpha = clave_publica["alpha"]
    a = clave_publica["a"]
    print(f"Clave publica del propietario: (p, alpha, a) = ({p}, {alpha}, {a})")

    mensaje = input("Escribe el mensaje a cifrar: ")

    cifrado = encriptar_mensaje(mensaje, p, alpha, a)
    guardar_json(cifrado, ARCHIVO_MENSAJE_CIFRADO)

    print(f"Mensaje cifrado y guardado en '{ARCHIVO_MENSAJE_CIFRADO}'.")
    print("Envia ese archivo al propietario para que lo desencripte.")


if __name__ == "__main__":
    main()
