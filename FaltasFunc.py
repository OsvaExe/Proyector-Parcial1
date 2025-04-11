def consultaFaltas():   
    while True:
        horas_semana=input("Por favor ingrese la cantidad de horas por semana [1-5] que tiene la materia en cuestion o 's' para salir \n\n:")
        try:
            horas_semana=int(horas_semana)
        except:
            if horas_semana=="s":
                break 
            print("Solo  entre 1 y 5 horas, no caracteres ")
            continue
        if 1<=horas_semana <=5:
            horas_totales= horas_semana*16
            print("Son ",horas_totales, " horas de clase por semestre " )        
        else:
            print("Las horas por semana tienen que ser en 1 a 5 horas \nvuelve a intentar ")
            continue
    
    #validacion de entrada de faltas
        faltas=input("Ingrese el numero de faltas: ")
        try:
            faltas=int(faltas)
        except:
            print("Solo numeros enteros")
            continue
    
    
        porcentaje_asistencia=(faltas/horas_totales)*100
        print("Porcentaje de asistencia = ",100-porcentaje_asistencia,"%")
    
        # el porcentaje es mayor a 80%
        if porcentaje_asistencia<=20:
            print("Tienes tienes derecho a ordinario y no ordinario")
            continue
    
        # si el procentaje de asistencia es menor que 60 no tiene derecho a nada
        if porcentaje_asistencia > 40:
            print("No tienes derecho a ordinario ni a no ordinario")
            continue

    #tiene entre 60 y 79.99 % de asistencia se va a no ordinario
    #si se tiene que ir a no ordinario verificar art 61 
        if porcentaje_asistencia >20 and porcentaje_asistencia <=40: # porcentaje de asistencia mayor que 60% pero menor que 80%
            while True:
                materias=input("¿Cuántas materias llevas? [1 - 8]:   o 's' para salir ")
                try:
                    materias=int(materias)
                    if materias<=0 or materias >=9:# validar que el numero de materias sea entre 1 y 8
                        print("El numero de materias tiene que ser entre 1 y 8, vuelve a intentar")
                        continue
                    elif materias==1:# si lleva solo una materia y tiene mas de 40% de faltas no tiene derecho a ordinario
                        print("solo llevas una materia y tienes ",porcentaje_asistencia,"'%' de faltas no hay nada que se pueda hacer\n no tienes derecho a no ordinarion ni a ordinario")
                        break
                    else:# tiene que tener minimo la mitad de materias aprobadas
                        materias_aporbadas=int(input("de esas cuantas pasaste: "))
                        if materias_aporbadas>= materias/2:
                            print("Como tiene menos de 80%, de asistencia pero cumples con el art 61 tienes derecho a no ordinarios")
                            break
                        else:
                            print("Aprobaste menos de la mitad de carga curricular que llevas este semestre \n no tienes derecho a no ordinarios, es hora de repetir materias")
                            break
                except:
                    if materias=="s":
                        break
                    else:
                        print("Solo numeros enteros del 1 a 8 materias")
                        continue

if __name__ == "__main__":
    consultaFaltas()