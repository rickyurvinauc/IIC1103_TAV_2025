nombre = input('Ingresa:')
# Ingresa:Ricardo
print(nombre)
# Ricardo
manzana = input('Ingresa:')
# Ingresa:100
x = manzana - 10
# Traceback (most recent call last):  
# File "<stdin>", line 1, in <module>
# TypeError: unsupported operand 
# type(s) for -: 'str' and 'int'
x = int(manzana) - 10
print(x)
# 90
