numeros = input("Dame numeros separados por coma: ")
lista = numeros.split(",")
l_aux = []
for i in lista:
    l_aux.append(int(i))

l_aux.sort()

print(l_aux)