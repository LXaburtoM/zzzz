def solicitar_entero_positivo(prompt):
    while True:
        valor = input(prompt)
        if valor.isdigit():
            return int(valor)
        else:
            print("Por favor, ingrese un número entero no negativo.")

def registrar_prestamos_usuario():
    categorias = {
        'Ingeniería': ['Eléctrica', 'Mecánica', 'Sistemas'],
        'Salud': ['Medicina', 'Enfermería', 'Odontología'],
        'Derecho': ['Penal', 'Civil', 'Constitucional'],
        'Literatura': ['Clásica', 'Moderna', 'Contemporánea']
    }
    dias = 5

    prestamos = {cat: {subcat: 0 for subcat in subs} for cat, subs in categorias.items()}

    print("Registro manual de préstamos por subcategoría y día:\n")
    for categoria, subcategorias in categorias.items():
        print(f"Categoría: {categoria}")
        for subcat in subcategorias:
            print(f"  Subcategoría: {subcat}")
            for dia in range(1, dias + 1):
                prompt = f"    Número de préstamos en día {dia}: "
                prestamos[categoria][subcat] += solicitar_entero_positivo(prompt)
            print(f"    Total préstamos subcategoría '{subcat}': {prestamos[categoria][subcat]}\n")

    totales_categoria = {}
    total_general = 0
    for categoria, subcats in prestamos.items():
        total_cat = sum(subcats.values())
        totales_categoria[categoria] = total_cat
        total_general += total_cat

    print("\nResumen de préstamos:\n")
    print(f"{'Categoría':<15} {'Subcategoría':<15} {'Préstamos':>10}")
    print("-" * 45)
    for categoria, subcats in prestamos.items():
        for subcat, total in subcats.items():
            print(f"{categoria:<15} {subcat:<15} {total:>10}")
        print(f"{'Total ' + categoria:<30} {totales_categoria[categoria]:>10}\n")
    print(f"{'Total General Semanal':<30} {total_general:>10}")

if __name__ == '__main__':
    registrar_prestamos_usuario()
