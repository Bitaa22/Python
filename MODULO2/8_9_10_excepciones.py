try:
    numero = int(input("Dame un numero: "))
    resultado = numero / 0
    print(resultado)
except ValueError:
    print("Tipo incorrecto")
except ZeroDivisionError:
    print("No se puede dividir entre cero")