num_clie=int(input('Ingrese el numero de clientes atendidos: '))

total_ventas= 0

for clientes in range(1,num_clie + 1):
    print(f'\nCliente #{clientes}')
    prociones= int(input('Cuantas porciones de vigoron compró: '))
    precio_uni= float(input('Cual es el precio por porción: '))

total_cli= prociones * precio_uni
print(f"  Total a pagar por el cliente #{clientes}: C$ {total_cli:.2f}")

total_ventas += total_cli

print(f"\nTotal general de ventas en la feria: C$ {total_ventas:.2f}")