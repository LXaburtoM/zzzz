
num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))


for estudiante in range(1, num_estudiantes + 1):
    print(f"\nEstudiante #{estudiante}")
    suma_promedios_asignaturas = 0

    
    for asignatura in range(1, 4):
        print(f"  Asignatura #{asignatura}")
        suma_tareas = 0

        
        for tarea in range(1, 4):
            nota_tarea = float(input(f"    Ingrese la nota de la tarea #{tarea}: "))
            suma_tareas += nota_tarea
        
        
        nota_examen = float(input("    Ingrese la nota del examen: "))

        
        promedio_asignatura = (suma_tareas + nota_examen) / 4
        print(f"    Promedio de la asignatura #{asignatura}: {promedio_asignatura:.2f}")

        
        suma_promedios_asignaturas += promedio_asignatura

    
    promedio_general = suma_promedios_asignaturas / 3
    print(f"  Promedio general del estudiante #{estudiante}: {promedio_general:.2f}")
