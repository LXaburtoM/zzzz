


carreras = ["Sistemas", "Marketing", "Derecho"]
anios = ["Primer Año", "Segundo Año", "Tercer Año"]
secciones = ["Sección A", "Sección B"]


participacion = {carrera: {anio: {seccion: 0 for seccion in secciones} for anio in anios} for carrera in carreras}


for carrera in carreras:
    print(f"\nRegistro para la carrera de {carrera}:")
    for anio in anios:
        print(f"  {anio}:")
        for seccion in secciones:
            while True:
                try:
                    cantidad = int(input(f"    Ingrese la cantidad de estudiantes en {seccion}: "))
                    if cantidad < 0:
                        print("    La cantidad no puede ser negativa. Intente nuevamente.")
                        continue
                    participacion[carrera][anio][seccion] = cantidad
                    break
                except ValueError:
                    print("    Entrada inválida. Por favor, ingrese un número entero.")


totales_por_carrera = {}
total_general = 0

print("\nResumen de participación:")
for carrera, anios_data in participacion.items():
    total_carrera = 0
    print(f"\nCarrera: {carrera}")
    for anio, secciones_data in anios_data.items():
        for seccion, cantidad in secciones_data.items():
            total_carrera += cantidad
    totales_por_carrera[carrera] = total_carrera
    total_general += total_carrera
    print(f"  Total de participantes: {total_carrera}")

print(f"\nTotal general de participantes: {total_general}")