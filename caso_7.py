def control_ventas_kioscos():
    kioscos = ["Kiosco 1", "Kiosco 2", "Kiosco 3"]
    productos = ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"]
    total_general = 0
    
    for dia in range(1, 5):  # 4 días
        print(f"\nRegistro de ventas para el día {dia}:")
        for kiosco in kioscos:
            total_kiosco = 0
            ventas_producto = [0] * len(productos)  # Inicializar ventas por producto
            
            for i, producto in enumerate(productos):
                cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {producto} en {kiosco}: "))
                ventas_producto[i] += cantidad_vendida
                total_kiosco += cantidad_vendida
            
            total_general += total_kiosco
            print(f"Total vendido en {kiosco} el día {dia}: {total_kiosco} productos")
            for i, producto in enumerate(productos):
                print(f"  {producto}: {ventas_producto[i]} unidades")
    
    print(f"Total general vendido en los {len(kioscos)} kioscos durante los 4 días: {total_general} productos")

# Llamar a la función
control_ventas_kioscos()
