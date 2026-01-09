def palindromo1(s):
    if s==s[::-1]:
        return True
    return False

def palindromo2(s):
    return s==s[::-1]

# Tests
print(palindromo1("oso")) # True
print(palindromo2("anita lava la tina")) # False
print(palindromo1("reconocer")) # True
print(palindromo2("hola")) # False
print(palindromo1("a")) # True
print(palindromo2("ab")) # False
print(palindromo1("abba")) # True