def consultaFaltas():
    # Datos iniciales
    total_clases = int(input("Introduce el número total de clases de una materia por semestre: "))
    asistencias = int(input("Introduce el número de asistencias del alumno: "))
    inasistencias = total_clases - asistencias

    # Cálculos de porcentaje
    porcentaje_asistencia = (asistencias / total_clases) * 100

    # Mensajes según los artículos
    if porcentaje_asistencia >= 80:
        print("El alumno tiene derecho a presentar el examen ordinario.")
    elif 60 <= porcentaje_asistencia < 80:
        print("El alumno tiene derecho a presentar el examen no ordinario.")
    elif porcentaje_asistencia < 60:
        print("El alumno debe repetir el curso y no tiene derecho a evaluaciones no ordinarias.")
    
    # Verificación adicional (artículo 61)
    carga_aprobada = int(input("Introduce el porcentaje de carga académica aprobada: "))
    if porcentaje_asistencia >= 60 and carga_aprobada >= 50:
        print("El alumno puede presentar evaluaciones no ordinarias.")
    else:
        print("El alumno no cumple con los requisitos para evaluaciones no ordinarias.")
if __name__ == "__main__":
    consultaFaltas()