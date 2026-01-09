str1 = "Hola"
str2 = 'ahí'
bob = str1 + str2
print(bob)
# Holaahí
str3 = '123'
str3 = str3 + 1
# Traceback (most recent call last):  
# File "<stdin>", line 1, in <module>
# TypeError: 
# cannot concatenate 'str' and 'int' objects
x = int(str3) + 1
print(x)
# 124

