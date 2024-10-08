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

# (Стешенко Станіслав КН-31.1)
# Головне меню для взаємодії з користувачем
def main():
    while True:
        print("\nМеню:")
        print("1. Додати нового студента")
        print("2. Вийти")

        choice = input("Виберіть дію (1-2): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Виклик головної функції для запуску програми
main()