frase = input("Introduce una frase")

contador = 0
for letra in frase:
   if(letra in "aeiouáéíóú"):
    contador = contador +1
print(contador)