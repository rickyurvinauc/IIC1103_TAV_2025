# Slicing
lista = []
lista = ['Ricardo','Ingrid','Liliana',29,29,50]
# recorrer sus elementos
# for item in lista:
#     print(item)

# recorrer por sus indices
# for  i_lista in range(len(lista)):
#     print("i lista", i_lista)
#     item = lista[i_lista]
#     print("item", item)

# lista_nombres = lista[:3]
# print(lista_nombres)
# lista_nueva = lista[1:10:2]
# # print("lista nueva", lista_nueva)
# # # concatenar listas
# lista3 = lista + lista_nueva
# print("lista concatenada", lista3)
# append
lista.append("Paul")
lista.append(["Anabelle","Medina"])
lista.append("Anabelle")
lista.append("Medina")
print("lista", lista)
# extend
lista.extend(["Anabelle", "Medina"])
print("lista con extend", lista)
# pop
eleminado = lista.pop(1)
print("Elemento eliminado", eleminado)
print("lista", lista)
# remove
lista.remove("Ricardo")
print("Lista remove", lista)
# in
existe_liliana = "liliana" in lista
print("Existe liliana", existe_liliana)
# sort
lista_numeros = [94,24,67,3]
lista_numeros.sort()
print("Numeros ordenados", lista_numeros)
lista_strings = ["Banana", "Zapato","Arco"]
lista_strings.sort()
print("Lista de strings ordenada", lista_strings)
# split
texto = "Hola;Ricardo;como;estas"
lista_texto = texto.split("a")
print("lista texto", lista_texto)


s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
print(s)
#spam-spam-spam