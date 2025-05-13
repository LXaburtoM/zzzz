facultades = {
    "Facultad de Ingeniería": ["Sistemas", "Industrial"],
    "Facultad de Ciencias Sociales": ["Derecho", "Psicología"],
    "Facultad de Negocios": ["Marketing", "Administración"]
}

# Definir los medios de transporte como claves de un diccionario
resultados = {facultad: {carrera: {"Bus": 0, "Motocicleta": 0, "Taxi": 0, "Bicicleta": 0, "Camina": 0} for carrera in carreras} for facultad, carreras in facultades.items()}

for facultad, carreras in facultades.items():
    print(f"\nEncuesta para la {facultad}:")
    for carrera in carreras:
        print(f"  Carrera: {carrera}")
        for estudiante in range(1, 6):  
            print(f"    Estudiante {estudiante}:")
            while True:
                print("      Medios de transporte disponibles:")
                print("        1. Bus")
                print("        2. Motocicleta")
                print("        3. Taxi")
                print("        4. Bicicleta")
                print("        5. Camina")
                try:
                    opcion = int(input("      Seleccione el medio de transporte (1-5): "))
                    if opcion == 1:
                        resultados[facultad][carrera]["Bus"] += 1
                        break
                    elif opcion == 2:
                        resultados[facultad][carrera]["Motocicleta"] += 1
                        break
                    elif opcion == 3:
                        resultados[facultad][carrera]["Taxi"] += 1
                        break
                    elif opcion == 4:
                        resultados[facultad][carrera]["Bicicleta"] += 1
                        break
                    elif opcion == 5:
                        resultados[facultad][carrera]["Camina"] += 1
                        break
                    else:
                        print("      Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("      Entrada inválida. Por favor, ingrese un número entero.")

totales_por_facultad = {}
total_general = {"Bus": 0, "Motocicleta": 0, "Taxi": 0, "Bicicleta": 0, "Camina": 0}

print("\nResumen de la encuesta:")
for facultad, carreras_data in resultados.items():
    print(f"\nFacultad: {facultad}")
    totales_por_facultad[facultad] = {"Bus": 0, "Motocicleta": 0, "Taxi": 0, "Bicicleta": 0, "Camina": 0}
    for carrera, medios_data in carreras_data.items():
        print(f"  Carrera: {carrera}")
        for medio, cantidad in medios_data.items():
            print(f"    {medio}: {cantidad}")
            totales_por_facultad[facultad][medio] += cantidad
            total_general[medio] += cantidad
    print(f"  Totales por facultad: {totales_por_facultad[facultad]}")

print("\nTotales generales por medio de transporte:")
for medio, cantidad in total_general.items():
    print(f"  {medio}: {cantidad}")