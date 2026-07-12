"""
.py
Funciones compartidas por el PROPIETARIO (quien recibe mensajes) y el
CLIENTE (quien los envía), siguiendo el criptosistema de ElGamal descrito
en el libro.

Alfabeto usado (códigos):
    A=0, B=1, ..., Z=25    (mayúsculas)
    a=26, b=27, ..., z=51  (minúsculas)
    espacio = 99
"""

import json
import secrets

# ---------------------------------------------------------------------
#? 1) Codificación letra <-> número (solo A-Z, a-z, y el espacio)
# ---------------------------------------------------------------------

TAM_ALFABETO = 52   #? 26 mayúsculas + 26 minúsculas
CODIGO_ESPACIO = 99  #? código fijo asignado al espacio (' ')


def es_letra(c):
    """True si c es una letra A-Z, a-z, o el espacio (' ')."""
    return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or c == ' '


def letra_a_codigo(c):
    """Convierte una letra (o el espacio) en su código numérico:
    A-Z -> 0..25, a-z -> 26..51, ' ' -> 99 (CODIGO_ESPACIO)."""
    if c == ' ':
        return CODIGO_ESPACIO
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A')          #? 0..25
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26     # ?26..51
    raise ValueError(f"'{c}' no es una letra A-Z/a-z ni el espacio")


def codigo_a_letra(n):
    """Convierte un código numérico de vuelta a su letra (o espacio)."""
    if n == CODIGO_ESPACIO:
        return ' '
    elif 0 <= n <= 25:
        return chr(n + ord('A'))
    elif 26 <= n <= 51:
        return chr(n - 26 + ord('a'))
    raise ValueError(f"Código {n} no reconocido")


# ---------------------------------------------------------------------
#? 2) Primalidad, primos y raíces primitivas
# 
# ---------------------------------------------------------------------

def es_primo(n, k=20):
    """Test de primalidad Miller-Rabin (probabilístico, suficiente para
    los tamaños que usamos en esta demostración)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n == p:
            return True
        if n % p == 0:
            return False

    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def primo_aleatorio(minimo, maximo):
    """Busca al azar un primo p en el rango [minimo, maximo].
    Debe cumplir p > CODIGO_ESPACIO (=99), que es el código más alto
    que se usa, para que cada bloque b < p."""
    if maximo <= minimo:
        raise ValueError("El rango dado es inválido")
    if minimo <= CODIGO_ESPACIO:
        raise ValueError(f"minimo debe ser mayor que {CODIGO_ESPACIO}")
    while True:
        candidato = secrets.randbelow(maximo - minimo) + minimo
        if candidato % 2 == 0:
            candidato += 1
        if candidato > minimo and es_primo(candidato):
            return candidato


def factorizar(n):
    """Factorización simple por división de prueba (n = p-1 no es
    demasiado grande en esta demostración)."""
    factores = set()
    d = 2
    m = n
    while d * d <= m:
        while m % d == 0:
            factores.add(d)
            m //= d
        d += 1
    if m > 1:
        factores.add(m)
    return factores


def raiz_primitiva(p):
    """Encuentra una raíz primitiva alpha de p, probando que
    alpha^((p-1)/q) != 1 (mod p) para cada factor primo q de p-1."""
    factores_p_menos_1 = factorizar(p - 1)
    for alpha in range(2, p):
        es_raiz = True
        for q in factores_p_menos_1:
            if pow(alpha, (p - 1) // q, p) == 1:
                es_raiz = False
                break
        if es_raiz:
            return alpha
    raise RuntimeError("No se encontró raíz primitiva (no debería pasar)")


# ---------------------------------------------------------------------
#? 3) Guardar / leer archivos JSON usados para "comunicarse"
# ---------------------------------------------------------------------

def guardar_json(datos, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
