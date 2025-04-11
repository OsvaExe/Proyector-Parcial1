#Código mediocre abajo
#esto es para hacer un commit
# Proyector-Parcial1
#Vamos a desarollar el proyecto de python del primer parcial
import sys 
import os
sys.path.append("C:\ProgramaP2\Proyector-Parcial1") #cambio de directorio de la función
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))    
from programa.promediop2 import promedio # importamos la funcion promedio
from FaltasFunc import consultaFaltas # importamos la funcion de faltas
## esto es un comentario para ver como se agrega al programa principal
#funcion para determinar la calificacion minima
def caliMin():
    print("Programa para determinar la calificacion minima del tercer parcial para acreditar")
    print("Por favor ingresa las dos calificaciones entre 0 y 10")
    while True:    #aqui validamos la calificacion
        try:
            calif1 = float(input("Primer calificación: ")) 
            if calif1 < 0 or calif1 > 10:
                print("Calificación NO válida")
                continue 
            calif2 = float(input("Segunda calificación: "))
            if calif2 < 0 or calif2 > 10:
                print("Calificación NO válida") 
                continue
            break
        except ValueError:
            print("El valor que tecleaste no es válido, debe ser un NUMERO DECIMAL entre 0 y 10.")
            continue
    calif3=((7-((calif1+calif2)*0.3))/0.4)# formula para obtener el valor requerido
    if calif3>10:
        print("En el 3er parcial debes obtener un: ", calif3)
        print("Ya no se puede hacer nada, lo siento \U0001F9D0 	")  
    elif calif3==10:
        print("En el 3er parcial debes obtener un: ", calif3)
        print("Si estas usando este programa no creo que lo logres, pero suerte.")
    elif calif3<5:
        print("En el 3er parcial debes obtener un: ",calif3)
        print("Quedate tranquilo") 
    else:
        print("En el 3er parcial debes obtener un: ",calif3)

# funcion para terminar el programa con opcion 5
def finalizar (): 
    print("hasta luego")
    terminar="si"
    return terminar
   

def inicio():
    terminar="no"
    while terminar == "no":
        print("Vamos a selecionar el procedimiento a ejecutar")
    # iniciamos la seleccion del programa y se valida la respuesta
        while True: 
            print("Selecciona \n 1 - Promedio \n 2 - tercer parcial \n 3 - Faltas \n 4 - NA's \n 5 - salir")    
            seleccion=input("ingresa un numero del 1 a 5: \n")
            try:
                seleccionint=int(seleccion)
                if 1 <= seleccionint <= 5:
                    print("El numero seleccionado fue: ", seleccionint)          
                else:
                    print("La seleccion debe ser entre 1 y 5 ")
                    continue
            except:
                print("Selecciona un numero de 1 a 5")
                continue
            break
        match seleccionint:
            case 1:
                print ("Obtener el promedio de tres evaluaciones.") 
                promedio()  
            case 2:
                print ("Califiacion minima del tercer parcial para acreditar la materia.")
                caliMin() 
            case 3:
                print ("Seleccionaste la función de Faltas")
                consultaFaltas()
            case 4:
                print("Seleccionaste la función de NA's.")
                while True:
                    try:
                        s = int(input("Ingresa tu semestre actual: "))
                        na = int(input("Ingresa el número de NA's que tienes acumulado: "))

                        if s < 1 or s > 9:
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
                        case _:
                            na7(na)
            case 5:
                print("Seleccionaste salir")
                terminar=finalizar()
    #   Aqui vamos a iniciar el programa
    

if __name__=="__main__":
    inicio()