"""
tuplas- a principal diferenca entre tuplas e listas e qua tuplas
nao podem ser alteradas, mas tuplas podem ser convertidas em listas
"""
t1 = (1,2,3,4,5)
print(type(t1))
t1 = list(t1)
print(type(t1))
t1 = tuple(t1)
print(type(t1))