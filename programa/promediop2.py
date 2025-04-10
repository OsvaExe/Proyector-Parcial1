#Programa para calcular el promedio de tres evaluaciones
def promedio():
    print("Por favor ingresa las calificaciones entre 0 y 10")
    while True:
        try:
            calif1 = float(input("Primer calificación: "))
            if calif1 < 0 or calif1 > 10:
                print("Calificación NO válida")
                continue
            calif2 = float(input("Segunda calificación: "))
            if calif2 < 0 or calif2 > 10:
                print("Calificación NO válida")
                continue
            calif3 = float(input("Tercera calificación: "))
            if calif3 < 0 or calif3 > 10:
                print("Calificación NO válida")
                continue
            break
        except ValueError:
            print("El valor que tecleaste no es válido, debe ser un NÚMERO DECIMAL entre 0 y 10.")
            continue
     
    promed = ((calif1*.3) + (calif2*.3) + (calif3*.4))
    print("El promedio es: ", promed)
    if promed == 10:
        print("Excelente!!!")
    elif promed >= 7:
        print("Aprobaste la materia", )
    elif promed == 0:
        print("Vete a conta bro \U0001F978")
    else:
        print("Reprobaste la materia")   
if __name__ == "__main__":
    promedio()