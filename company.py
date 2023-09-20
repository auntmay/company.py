"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},

]

print(1)

# 1. Вывести названия всех отделов.

for elements in departments: 
    print(elements['title'])

print(2)

# 2. Вывести имена всех сотрудников компании.

for department in departments:
    for employers in department['employers']:
        print(employers['first_name'])

print(3)

# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.

for department in departments:
    for employers in department['employers']:
        print(f'{employers["first_name"]} работает в {department["title"]}')

print(4)

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.

list_100kmoresalary_names = []

for department in departments:
    for employers in department['employers']:
        if employers['salary_rub'] > 100000:
            list_100kmoresalary_names.append(employers["first_name"])

print(f"Имена сотрудников, которые получают > 100.000 р.: {', '.join(list_100kmoresalary_names)}")

# 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)

print(5)

list_100kmoresalary_positions = []

for department in departments:
    for employers in department['employers']:
        if employers['salary_rub'] < 100000:
            list_100kmoresalary_positions.append(employers["position"])

print(f"Позиции, на которых получают < 100.000 р.: {', '.join(list_100kmoresalary_positions)}")
            
# 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

print(6)

for department in departments:
    dep_salary = 0
    for employers in department['employers']:
        dep_salary += employers['salary_rub']
    print(f"Зарплатный фонд {department['title']} = {dep_salary} р.")

# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.

print(7)

for department in departments:
    print(f"Минимальная зарплата в {department['title']} = {min([employer['salary_rub'] for employer in department['employers']])}")


# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.

print(8)

for department in departments:
    print(department['title'])
    print(f"Минимальная зарплата = {min([employer['salary_rub'] for employer in department['employers']])} р.")
    print(f"Средняя зарплата = {(sum([employer['salary_rub'] for employer in department['employers']]))/len(department)} р.")
    print(f"Максимальная зарплата = {max([employer['salary_rub'] for employer in department['employers']])} р.")
    print()

# 9. Вывести среднюю зарплату по всей компании.

print(9)

employee_count = 0
salary_sum_9 = 0

for department in departments:
    salary_sum_9 += sum([employer['salary_rub'] for employer in department['employers']])
    employee_count += len(department['employers'])

print(f"Средняя зарплата в company = {salary_sum_9 / employee_count} р.")

# 10. Вывести названия должностей, которые получают больше 90к без повторений.

print(10)

positions_dict = {}

for department in departments:
    for employee in department["employers"]:
        if employee['position'] not in positions_dict.keys():
            if employee['salary_rub'] > 90000:
                positions_dict[employee['position']] = employee['salary_rub']
        else:
            if employee['salary_rub'] > positions_dict[employee['position']]:
                positions_dict[employee['position']] = employee['salary_rub']

print(f'Список позиций, на которых получают > 90.000 р: {", ".join(list(position for position in positions_dict.keys()))}')

print(11)

# 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).

is_female = ['Michelle', 'Nicole', 'Christina', 'Caitlin']

for department in departments:
    females_salary_list = [name['salary_rub'] for name in department['employers'] if name['first_name'] in is_female]
    females_salary_sum = sum(females_salary_list)
    female_department_count = len(females_salary_list)
    print(f"Средняя зарплата девушек в отделе {department['title']} = {females_salary_sum/female_department_count}")

print(12)

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

vowels_list = 'aeiouy'
result_list = []
for department in departments:
    result_list += list(set([employee['last_name'] for employee in department['employers'] if employee['last_name'][-1] in vowels_list]))

print(', '.join(result_list))

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},

]

# 13. Вывести список отделов со средним налогом на сотрудников этого отдела.

print(13)

dep_taxes_list = {dep["department"].lower():dep["value_percents"] for dep in taxes[1:]}
default_tax_13perc = taxes[0]['value_percents'] / 100

for department in departments:

    salary_sum_13 = sum([employee['salary_rub'] for employee in department['employers']])
    
    if department['title'].lower() in dep_taxes_list.keys():
        current_dep_tax = dep_taxes_list[department['title'].lower()] / 100
        print(f"Средний налог в отделе {department['title']} = {salary_sum_13 * (current_dep_tax + default_tax_13perc)} рублей.")
    else:
        print(f"Средний налог в отделе {department['title']} = {salary_sum_13 * default_tax_13perc} рублей.")


# 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.

print(14)

for department in departments:
    for employee in department['employers']:
        if department['title'].lower() in dep_taxes_list.keys():
            current_dep_tax = dep_taxes_list[department['title'].lower()] / 100
            print(f"{employee['first_name']} зарабатывает {employee['salary_rub']} р. (с вычетом = {employee['salary_rub'] * (1 - (default_tax_13perc + current_dep_tax))})")
        else:
            print(f"{employee['first_name']} зарабатывает {employee['salary_rub']} р. (с вычетом = {employee['salary_rub'] * (1 - default_tax_13perc)})")


# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.

print(15)

tax_dict_15 = {}

for department in departments:
    if department['title'].lower() in dep_taxes_list.keys():
        current_dep_tax = dep_taxes_list[department['title'].lower()] / 100
        salary_dep_sum_15 = sum([employee['salary_rub'] for employee in department['employers']]) * (default_tax_13perc + current_dep_tax)
    else:
        salary_dep_sum_15 = sum([employee['salary_rub'] for employee in department['employers']]) * default_tax_13perc

    tax_dict_15[department['title']] = salary_dep_sum_15

sorted_tax_dict = sorted(tax_dict_15.items(), key = lambda x : x[1], reverse=True)
print(sorted_tax_dict)

# 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

print(16)

tax_dict_16 = {}

for department in departments:   
    for employee in department['employers']:
        
        if department['title'].lower() in dep_taxes_list.keys():
            current_dep_tax = dep_taxes_list[department['title'].lower()] / 100
            employee_year_tax = employee['salary_rub'] * (default_tax_13perc + current_dep_tax) * 12
            if employee_year_tax > 100000:
                tax_dict_16[f"{employee['first_name']} {employee['last_name']}"] = employee_year_tax
        
        else:
            employee_year_tax = employee['salary_rub'] * default_tax_13perc * 12
            if employee_year_tax > 100000:
                tax_dict_16[f"{employee['first_name']} {employee['last_name']}"] = employee_year_tax

print(sorted(tax_dict_16.items(), key = lambda x: x[1], reverse=True))

# 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

print(17)

tax_dict_17 = {}

for department in departments:   
    for employee in department['employers']:
        
        if department['title'].lower() in dep_taxes_list.keys():
            current_dep_tax = dep_taxes_list[department['title'].lower()] / 100
            employee_tax = employee['salary_rub'] * (default_tax_13perc + current_dep_tax)
            
            tax_dict_17[f"{employee['first_name']} {employee['last_name']}"] = employee_tax
        
        else:
            employee_tax = employee['salary_rub'] * default_tax_13perc
            tax_dict_17[f"{employee['first_name']} {employee['last_name']}"] = employee_tax

print((sorted(tax_dict_17.items(), key = lambda x: x[1]))[0])

