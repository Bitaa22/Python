alumno = {
        "nombre": "Alba",
        "edad": 30,
        "curso": "DAW"
    }

print(f"Alumno: {alumno['nombre']}")
print(f"Edad: {alumno['edad']}")
print(f"Curso: {alumno['curso']}")

print(*alumno, sep=", ")