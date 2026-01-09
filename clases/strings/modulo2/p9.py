def son_llave(p, q):
    mayusculas = 'AEIOU'
    for ip in range(len(p)):
        if (p[ip] in mayusculas) != (q[ip] in mayusculas):
            return False
    return True

def casi_llave(p, q):
    largo_q = len(q)
    for i in range(len(p)):
        if largo_q + i > len(p):
            break
        p_cortada = p[i:largo_q + i]
        res_son_llave = son_llave(p_cortada, q)
        if res_son_llave:
            return True
    return False