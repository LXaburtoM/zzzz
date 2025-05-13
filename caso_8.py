def registro_consumo_electrico():
    edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]
    turnos = ["Mañana", "Tarde", "Noche"]
    consumo_semanal = {edificio: 0 for edificio in edificios}
    
    for dia in range(1, 8):  # 7 días
        print(f"\nRegistro de consumo para el día {dia}:")
        for edificio in edificios:
            consumo_diario = 0
            
            for turno in turnos:
                consumo = float(input(f"Ingrese el consumo eléctrico en {edificio} durante el turno de {turno}: "))
                consumo_diario += consumo
            
            consumo_semanal[edificio] += consumo_diario
            print(f"Consumo total en {edificio} el día {dia}: {consumo_diario} kWh")
    
    print("\nConsumo total semanal por edificio:")
    for edificio, total in consumo_semanal.items():
        print(f"{edificio}: {total} kWh")

# Llamar a la función
registro_consumo_electrico()
