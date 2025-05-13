
facultades = {
    "Facultad de Ingeniería": ["Sistemas", "Industrial"],
    "Facultad de Ciencias Sociales": ["Derecho", "Psicología"],
    "Facultad de Negocios": ["Marketing", "Administración"]
}
medios_transporte = ["Bus", "Motocicleta", "Taxi", "Bicicleta", "Camina"]

resultados = {facultad: {carrera: {medio: 0 for medio in medios_transporte} for carrera in carreras} for facultad, carreras in facultades.items()}

for facultad, carreras in facultades.items():
    print(f"\nEncuesta para la {facultad}:")
    for carrera in carreras:
        print(f"  Carrera: {carrera}")
        for estudiante in range(1, 6):  
            print(f"    Estudiante {estudiante}:")
            while True:
                print("      Medios de transporte disponibles:")
                for i, medio in enumerate(medios_transporte, start=1):
                    print(f"        {i}. {medio}")
                try:
                    opcion = int(input("      Seleccione el medio de transporte (1-5): "))
                    if 1 <= opcion <= 5:
                        medio_seleccionado = medios_transporte[opcion - 1]
                        resultados[facultad][carrera][medio_seleccionado] += 1
                        break
                    else:
                        print("      Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("      Entrada inválida. Por favor, ingrese un número entero.")


totales_por_facultad = {}
total_general = {medio: 0 for medio in medios_transporte}

print("\nResumen de la encuesta:")
for facultad, carreras_data in resultados.items():
    print(f"\nFacultad: {facultad}")
    totales_por_facultad[facultad] = {medio: 0 for medio in medios_transporte}
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