# Escribe tu código aquí
from dccaja import imprimir_caja

peso_max = int(input())
canti_muestras = int(input())

mi_caja = Caja(peso_max) # mi caja es un objeto de tipo Caja

for indice_m in range(canti_muestras):
    tipo = input()
    peso = int(input())
    fragil = int(input())# 1 o 0

    if fragil == 1:
        fragil = True
    else:
        fragil = False
    
    mi_muestra = Muestra(tipo, peso, fragil)
    mi_caja.agregar_muestra(mi_muestra)


imprimir_caja(mi_caja)
