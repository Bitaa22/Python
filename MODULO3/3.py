frutas = ["Sandía", "Melocotón", "Kiwi", "Naranja", "Papaya"]

print(frutas)

print("Primer elemento: ", frutas[0])
print("Primer elemento: ", frutas[-1])

print("Número de elementos: ", len(frutas))

frutas.append("Fresa")

print(frutas)

for fruta in frutas:
    print(fruta)

print(*frutas, sep=", ")