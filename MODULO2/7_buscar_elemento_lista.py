videojuegos = ["Zelda", "Mario", "Stardew valley"]

buscar = input("Introduce el nombre de un videojuego").lower().strip()

encontrado = False

for juego in videojuegos:
    if(juego.lower() == buscar):
        print("Juego encontrado")
        print(juego)
        encontrado = True
        break
    else: 
        print("Juego no encontrado")
        break
