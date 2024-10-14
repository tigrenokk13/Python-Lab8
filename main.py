# (Стешенко Станіслав КН-31.1)
# Словник для зберігання даних про студентів
students = {
    "Стешенко Станіслав Олександрович": {
        "group": "КН-31.1",
        "course": 2,
        "grades": {
            "Програмування": 5,
            "Алгоритми": 4,
            "Чисельні методи": 4
        }
    },
    "Іванченко Олександр Ігорович": {
        "group": "КН-33-2",
        "course": 2,
        "grades": {
            "Математичні методи": 5,
            "Чисельні методи": 4
        }
    },
    "Шелест Ігор Андрійович":{
        "group": "КН-33-2",
        "course": 2,
        "grades": {
            "Математичні методи": 4,
            "Чисельні методи": 4
            }
    }
}

# (Стешенко Станіслав КН-31.1)
# Функція для додавання інформації про нового студента
def add_student():
    pib = input("Введіть ПІБ студента: ")
    if pib in students:
        print(f"Студент '{pib}' вже існує у словнику.")
    else:
        try:
            group = input("Введіть номер групи: ")
            course = int(input("Введіть курс (число): "))
            subjects_count = int(input("Кількість предметів: "))

            grades = {}
            for _ in range(subjects_count):
                subject = input("Назва предмета: ")
                grade = int(input("Оцінка за предмет (1-5): "))
                grades[subject] = grade

            students[pib] = {
                "group": group,
                "course": course,
                "grades": grades
            }
            print(f"Запис додано: {pib}")
        except ValueError:
            print("Помилка: Невірний формат введених даних.")

# (Іванченко Олександр КН-33-2)
# Функція для видалення студента
def remove_student():
    pib = input("Введіть ПІБ студента, якого ви хочете видалити: ")
    if pib in students:
        del students[pib]
        print(f"Студента '{pib}' видалено.")
    else:
        print(f"Студент '{pib}' не знайдений.")

# (Іванченко Олександр КН-33-2)
# Функція для виводу студентів на екран
def display_students(sorted_students=None):
    if sorted_students is None:
        sorted_students = students

    if not sorted_students:
        print("Немає студентів для відображення.")
    else:
        for pib, info in sorted_students.items():
            print(f"\nПІБ: {pib}")
            print(f"Група: {info['group']}")
            print(f"Курс: {info['course']}")
            print("Оцінки:")
            for subject, grade in info['grades'].items():
                print(f"  {subject}: {grade}")


#(Шелест Ігор КН-33/2)
# Нова функція для редагування оцінок студента
def edit_grades():
    pib = input("Введіть ПІБ студента, оцінки якого ви хочете змінити: ")
    if pib in students:
        grades = students[pib]["grades"]
        for subject in grades:
            new_grade = int(input(f"Нова оцінка за {subject} (1-5): "))
            if 1 <= new_grade <= 5:
                grades[subject] = new_grade
            else:
                print("Помилка: Оцінка повинна бути в діапазоні від 1 до 5.")
        print(f"Оцінки студента '{pib}' оновлені.")
    else:
        print(f"Студент '{pib}' не знайдений.")


                
# (Стешенко Станіслав КН-31.1)
# Головне меню для взаємодії з користувачем
def main():
    while True:
        print("\nМеню:")
        print("1. Додати нового студента")
        print("2. Показати всіх студентів")
        print("3. Видалити студента")
        print("4. Редагувати оцінки студента")
        print("5. Вийти")

        choice = input("Виберіть дію (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            edit_grades()
        elif choice == "5":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Виклик головної функції для запуску програми
main()




