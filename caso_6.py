def registro_ventas_nacatamales():
    total_acumulado = 0
    for domingo in range(1, 5):  # 4 domingos
        cantidad_clientes = int(input(f"Ingrese la cantidad de clientes para el domingo {domingo}: "))
        total_domingo = 0
        
        for cliente in range(1, cantidad_clientes + 1):
            nacatamales_comprados = int(input(f"Ingrese la cantidad de nacatamales comprados por el cliente {cliente}: "))
            total_domingo += nacatamales_comprados
        
        total_acumulado += total_domingo
        print(f"Total vendido el domingo {domingo}: {total_domingo} nacatamales")
    
    print(f"Total acumulado mensual: {total_acumulado} nacatamales")

# Llamar a la función
registro_ventas_nacatamales()
