lista = ["Alba", "Mao", "Jua", "Alejandro", "Mario"]

#UTILIZANDO FOR
for nombre in lista:
    if(len(nombre.lower()) >= 4):
        print(nombre, end=", ")

#IMPRIMIR LISTA 
print(*lista, sep=", ")