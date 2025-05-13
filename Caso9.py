import random
def simulate_survey():
    careers = ['Ingeniería', 'Administración', 'Diseño']
    groups_per_career = 3
    students_per_group = 5
    access_types = ['estable', 'intermitente', 'sin internet']
    # Data structure: dict of careers -> counters of access types
    results = {career: {atype: 0 for atype in access_types} for career in careers}
    total_counts = {atype: 0 for atype in access_types}
    for career in careers:
        print(f'Encuestando la carrera: {career}')
        for group_num in range(1, groups_per_career + 1):
            print(f'  Grupo {group_num}')
            for student_num in range(1, students_per_group + 1):
                access = random.choice(access_types)
                results[career][access] += 1
                total_counts[access] += 1
                print(f'    Estudiante {student_num}: acceso {access}')
        print()
    print('\nResumen de resultados por carrera:')
    print(f'{"Carrera":<15} {"Estable":>8} {"Intermitente":>15} {"Sin internet":>15}')
    print('-' * 55)
    for career in careers:
        r = results[career]
        print(f'{career:<15} {r["estable"]:>8} {r["intermitente"]:>15} {r["sin internet"]:>15}')
    print('-' * 55)
    print(f'{"Total General":<15} {total_counts["estable"]:>8} {total_counts["intermitente"]:>15} {total_counts["sin internet"]:>15}')
if __name__ == '__main__':
    simulate_survey()