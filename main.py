"""
Точка входа в программу "Бюджетный помощник". 

Модуль нужен для:
1. Запуск всей программы
2. Вывод меню для пользователя
3. Обработки действий пользователя
4. Загрузки тестовых данных из csv-файла
"""

import csv 
from manager import BudgetManager

TEST_DATA_FILE = "expenses.csv"

def print_menu():
    """Функция выводит главное меню программы"""

    print("\n=== БЮДЖЕТНЫЙ ПОМОЩНИК ===\n")
    print("1. Загрузить тестовые данные за последние 31 день")
    print("2. Добавить расход")
    print("3. Показать все расходы")
    print("4. Посчитать расходы за период")
    print("5. Найти день с максимальными расходами")
    print("6. Показать расходы по категориям")
    print("7. Отменить последнее добавление")
    print("8. Показать расходы из дерева")
    print("0. Выход")

def read_int(promt):
    """
    Считывает ввод пользователя - целое число с клавиатуры.
    В качестве аргумента принимает promt - текст, который выведется пользователю
    Возвращает целое число, введенное пользователем.
    """
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print ("Ошибка! Нужно ввести целое число.")

def read_float(promt):
    """
    Считывает ввод пользователя - вещественное число с клавиатуры.
    В качестве аргумента принимает promt - текст, который выведется пользователю
    Возвращает вещественное число, введенное пользователем.
    """
    while True:
        try:
            return float(input(promt))
        except ValueError:
            print ("Ошибка! Нужно ввести число.")

def format_amount(amount):
    """
    Форматирует сумму для красивого вывода.
    Принимает в качестве аргумента amount - сумму расхода.
    Возвращает строку с суммой без лишнего .0, если число целое.
    """
    # Если число целое, преобразуем его в int
    if amount == int(amount):
        return str(int(amount))

    # Если число не целое, округляем его
    return str(round(amount, 2))

def load_test_data(manager, filename):
    """
    Загружает тестовые расходы из CSV-файла
    CSV-файл используется только для быстрого заполнения программы
    начальными данными. Все загруженные расходы добавляются через add_expense()
    Принимает в качестве аргументов:
        manager: объект BudgetManager.
        filename: имя CSV-файла.
    """
    try:
        # Открываем csv-файл для чтения
        with open(filename, "r", encoding="utf-8") as file:
            # DictReader читает CSV как словарь
            reader = csv.DictReader(file)
            loaded_count = 0

            # Достаем значения из строки файла
            for row in reader:
                day = int(row["day"])
                amount = float(row["amount"])
                category = row["category"].strip()

                # Добавляем новый расход
                manager.add_expense(day, amount, category)
                loaded_count += 1

        print(f"Загружено расходов: {loaded_count}")

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")

def handle_add_expense(manager):
    """
    Обрабатывает ручное добавление расхода
    Принимает в качестве аргумента manager: объект BudgetManager
    """
    # Считываем данные пользователя
    day = read_int("Введите день месяца от 1 до 31: ")
    amount = read_float("Введите сумму расхода: ")
    category = input("Введите категорию расхода: ").strip()

    # Добавляем новый расход 
    expense = manager.add_expense(day, amount, category)
    print(f"Расход добавлен: {expense}")

def handle_show_expenses(manager):
    """
    Выводит все добавленные расходы
    Принимает в качестве аргумента manager: объект BudgetManager.
    """
    # Получаем список расходов из manaher
    expenses = manager.get_all_expenses()

    # Если список пустой, выводить нечего
    if not expenses:
        print("Расходов пока нет.")
        return

    # Используем enumerate, чтобы красиво пронумеровать расходы с 1
    print("\nВсе расходы:\n")
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense}")

def handle_period_sum(manager):
    """
    Выводит сумму расходов за выбранный период.
    Принимает в качестве аргумента manager: объект BudgetManager.
    """
    # Считываем данные пользователя
    start_day = read_int("Введите начальный день: ")
    end_day = read_int("Введите конечный день: ")

    # Manager использует префиксные суммы и возвращает результат
    total = manager.get_period_sum(start_day, end_day)
    # Форматируем сумму
    total = format_amount(total)

    print(f"Сумма расходов с {start_day} по {end_day} день: {total} руб.")

def handle_max_day(manager):
    """
    Выводит день с максимальной суммой расходов.
    Принимает в качестве аргумента manager: объект BudgetManager.
    """
    # Получаем день и сумму расходов за заданный день
    day, amount = manager.get_max_expense_day()

    # Если сумма 0, то расходов пока нет
    if amount == 0:
        print("Расходов пока нет.")
        return

    # Форматируем сумму 
    amount = format_amount(amount)
    print(f"Больше всего потрачено в {day} день: {amount} руб.")


def handle_categories(manager):
    """
    Выводит категории расходов, отсортированные по сумме
    Принимает в качестве аргумента manager: объект BudgetManager.
    """
    # Получаем категории, отсортированные вставками
    categories = manager.get_sorted_categories()

    # Если список пуст, расходов пока нет
    if not categories:
        print("Расходов пока нет")
        return

    print("\nРасходы по категориям:")

    # Выводим категории и суммы нумерованным списком
    for number, category_data in enumerate(categories, start=1):
        category = category_data[0]
        amount = format_amount(category_data[1])

        print(f"{number}. {category} — {amount} руб.")


def handle_undo(manager):
    """
    Отменяет последнее добавление расхода
    Принимает в качестве аргумента manager: объект BudgetManager.
    """
    # Достаем последний добавленный элемент стека
    deleted_expense = manager.undo_last_expense()

    # Если стек пустой, значит расходов еще нет 
    if deleted_expense is None:
        print("Отменять нечего")
        return

    print(f"Отменён расход: {deleted_expense}")


def handle_tree_expenses(manager):
    """
    Выводит расходы из дерева в порядке возрастания дней
    Принимает в качестве аргумента manager: объект BudgetManager.
    """
    # Получаем расходы через симметричный обход дерева
    expenses = manager.get_tree_expenses()

    # Если дерево пустое, то расходов пока нет
    if not expenses:
        print("Дерево пустое. Расходов пока нет")
        return

    print("\nРасходы из дерева по дням:")

    # Выводим траты последовательно
    for expense in expenses:
        print(expense)


def main():
    """
    Запускает программу и обрабатывает выбор пользователя
    """
    # Создаём главный объект, который будет хранить все данные программы
    manager = BudgetManager()

    # Бесконечный цикл, чтобы меню показывалось пока пользователь не выберет выход
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            load_test_data(manager, TEST_DATA_FILE)

        elif choice == "2":
            handle_add_expense(manager)

        elif choice == "3":
            handle_show_expenses(manager)

        elif choice == "4":
            handle_period_sum(manager)

        elif choice == "5":
            handle_max_day(manager)

        elif choice == "6":
            handle_categories(manager)

        elif choice == "7":
            handle_undo(manager)

        elif choice == "8":
            handle_tree_expenses(manager)

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Ошибка: такого пункта меню нет.")

# Конструкция для запуска программы
if __name__ == "__main__":
    main()
