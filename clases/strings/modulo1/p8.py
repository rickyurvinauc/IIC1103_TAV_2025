# Escribe tu código aquí
def son_llave(p, q):
    mayusculas = 'AEIOU'
    for ip in range(len(p)):
        if (p[ip] in mayusculas) != (q[ip] in mayusculas):
            return False
    return True