try:
    archivo = open("noexiste.py", "r")
except:
    print("ERROR")
finally:
    if archivo:
        archivo.close()
    print("FINALIZADO")