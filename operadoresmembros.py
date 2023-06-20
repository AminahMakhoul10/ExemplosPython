lista = [1, 2, 3, 'Ana', 'Carla']    #operador de membro
2 in lista
"Ana" not in lista                    #not in = nao está na lista

#operador de identidade

x = 3
y = x
z = 3
y is z
x is not z

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a
lista_a is lista_b