#esto es para hacer un commit
# Proyector-Parcial1
#Vamos a desarollar el proyecto de python del primer parcial
#import sys
#import os4
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))
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
                print ("faltas")
            case 4:
                print("NA's")
            case 5:
                #print("final")
                terminar=finalizar()
    #   Aqui vamos a iniciar el programa
    

if __name__=="__main__":
    inicio()
