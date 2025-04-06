#Código mediocre abajo
#esto es para hacer un commit
# Proyector-Parcial1
#Vamos a desarollar el proyecto de python del primer parcial
import sys 
import os
## esto es un comentario para ver como se agrega al programa principal
def finalizar ():
    print("hasta luego")
    terminar="si"
    return terminar


def inicio():
    terminar="no"
    while terminar == "no":
        print("vamos a selecionar el procedimiento a ejecutar")
    # iniciamos la seleccion del programa y se valida la respuesta
        while True: 
            print("Selecciona \n 1 - Promedio \n 2 - tercer parcial \n 3 - Faltas \n 4 - NA's \n 5 - salir")    
            seleccion=input("ingresa un numero del 1 a 5: \n")
            try:
                seleccionint=int(seleccion)
                if 1 <= seleccionint <= 5:
                    print("el numero seleccionado fue: ", seleccionint)          
                else:
                    print("la seleccion debe ser entre 1 y 5 ")
                    continue
            except:
                print("selecciona un numero de 1 a 5")
                continue
            break
        match seleccionint:
            case 1:
                print ("promedio")
            case 2:
                print ("tercer parcial")
            case 3:
                print ("Faltas")
            case 4:
                print("NA's")
                while True:
                    try:
                        s = int(input("Ingresa tu semestre actual: "))
                        na = int(input("Ingresa el número de NA's que tienes acumulado: "))

                        if s < 1 or s > 8:
                            print("El semestre debe ser mayor a 0 y menor que 9.")
                            continue
                        if na < 0:
                            print("El número de NA no debe ser menor que 0.")
                            continue
                        break
                    except ValueError:
                        print("El valor que tecleaste no es válido, debe ser un numero ENTERO mayor o igual a 0 segun sea el caso. Intente de nuevo.")

                if s <= 5:
                    def na5(na):
                        if na >= 8:
                            print("Estás en baja definitiva")
                        elif 5 <= na <= 7:
                            print("Estás en riesgo")
                        elif 0 <= na <= 4:
                            print("Todo bien")
                    na5(na)
                else:
                    def na7(na):
                        if na >= 11:
                            print("Estás en baja definitiva")
                        elif 9 <= na <= 10:
                            print("Estás en riesgo")
                        elif 0 <= na <= 8:
                            print("Todo bien")
                    na7(na)
                    match s:
                        case 6:
                            if na >= 10:
                                print("Estás en baja definitiva")
                            elif 7 <= na <= 9:
                                print("Estás en riesgo")
                            elif 0 <= na <= 6:
                                print("Todo bien")
                        case 7:
                            na7(na)
                        case _:
                            na7(na)
            case 5:
                print("final")
                terminar=finalizar()
    #   Aqui vamos a iniciar el programa
    

if __name__=="__main__":
    inicio()
