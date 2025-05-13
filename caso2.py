total_mensual = 0

for semana in range(1, 5):
    print(f"\nSemana #{semana}")
    total_semana = 0
    
    
    for dia in range(1, 8):
        gasto_dia = float(input(f"  Ingrese el gasto del día {dia}: C$ "))
        total_semana += gasto_dia

    
    print(f"  Total gastado en la semana #{semana}: C$ {total_semana:.2f}")
    
    
    total_mensual += total_semana

print(f"\nTotal acumulado del mes: C$ {total_mensual:.2f}")
