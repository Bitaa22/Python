def media(a, b):
    return (a + b) / 2

try:
    x = int(input("Dame primer numero: "))
    y = int(input("Dame segundo numero: "))
except ValueError:
    print("ERROR")

resultado = media(x, y)
print(resultado)