# Escribe tu código aquí

minusculas = 'aeiou'
palabra = input()
contador = 0
for letra in palabra:
    for l in minusculas:
        if letra == l:
            contador += 1
            break
print(contador)


