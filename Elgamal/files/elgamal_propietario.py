"""
elgamal_propietario.py
-----------------------
Este es el programa de la persona A ("el propietario"):
quien desea RECIBIR mensajes cifrados.

"""

from elgamal_comun import (
    TAM_ALFABETO,
    codigo_a_letra,
    es_primo,
    primo_aleatorio,
    raiz_primitiva,
    guardar_json,
    leer_json,
)

ARCHIVO_CLAVE_PUBLICA = "clave_publica.json"
ARCHIVO_CLAVE_PRIVADA = "clave_privada.json"
ARCHIVO_MENSAJE_CIFRADO = "mensaje_cifrado.json"


def generar_claves():
    """Paso 1 del libro: genera (p, alpha, a) públicos y e secreto."""
    #? p debe ser mayor que TAM_ALFABETO (52) para que cada bloque b < p.
    #? Usamos un rango moderado para que el ejemplo corra rápido; para uso
    #? real se usaría un primo mucho más grande.
    p = primo_aleatorio(1000, 5000)
    alpha = raiz_primitiva(p)
    e = secrets_randbelow_1_a_pmenos1(p)
    a = pow(alpha, e, p)

    clave_publica = {"p": p, "alpha": alpha, "a": a}
    clave_privada = {"e": e}

    guardar_json(clave_publica, ARCHIVO_CLAVE_PUBLICA)
    guardar_json(clave_privada, ARCHIVO_CLAVE_PRIVADA)

    print("Claves generadas correctamente.")
    print(f"  Clave publica  (p, alpha, a) = ({p}, {alpha}, {a})")
    print(f"    -> guardada en '{ARCHIVO_CLAVE_PUBLICA}' (compartir con el cliente)")
    print(f"  Clave secreta  e = {e}")
    print(f"    -> guardada en '{ARCHIVO_CLAVE_PRIVADA}' (NO compartir, solo el propietario la usa)")


def secrets_randbelow_1_a_pmenos1(p):
    """Genera e con 1 <= e <= p-1, como pide el libro."""
    import secrets
    return secrets.randbelow(p - 1) + 1


def desencriptar_mensaje():
    """Paso 3 del libro: usa la clave secreta e para desencriptar."""
    try:
        clave_publica = leer_json(ARCHIVO_CLAVE_PUBLICA)
        clave_privada = leer_json(ARCHIVO_CLAVE_PRIVADA)
        cifrado = leer_json(ARCHIVO_MENSAJE_CIFRADO)
    except FileNotFoundError as err:
        print(f"Falta un archivo necesario: {err.filename}")
        return

    p = clave_publica["p"]
    e = clave_privada["e"]
    gamma = cifrado["gamma"]

    #? gamma^(-e) = gamma^(p-1-e) (mod p)   -- fórmula exacta del libro
    gamma_inv_e = pow(gamma, p - 1 - e, p)

    texto_plano = []
    for bloque in cifrado["bloques"]:
        if bloque["tipo"] == "cifrado":
            beta = bloque["beta"]
            b = (gamma_inv_e * beta) % p          # recupera el bloque b
            texto_plano.append(codigo_a_letra(b))  # bloque b -> letra
        else:  # "literal": caracter que no era letra, va sin cifrar
            texto_plano.append(bloque["valor"])

    mensaje = "".join(texto_plano)
    print("Mensaje desencriptado:")
    print(f"  {mensaje}")
    return mensaje


def menu():
    print("=== ElGamal - Propietario (persona A) ===")
    print("1) Generar par de claves (publica/privada)")
    print("2) Desencriptar mensaje recibido (mensaje_cifrado.json)")
    opcion = input("Elige una opcion (1/2): ").strip()
    if opcion == "1":
        generar_claves()
    elif opcion == "2":
        desencriptar_mensaje()
    else:
        print("Opcion invalida.")


if __name__ == "__main__":
    menu()
