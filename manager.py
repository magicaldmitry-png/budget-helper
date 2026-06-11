"""
Основная логика программы "Бюджетный помощник"

Модуль содержит класс BudgetManager, который управляет расходами,
стеком отмены, деревом расходов, дневными суммами и префиксными суммами.
"""

from algorithms import build_daily_totals, build_prefix_sums
from models import Expense
from structures import Stack, ExpenseTree

class BudgetManager:
    def __init__(self):
        """
        Создает пустой менеджер расходов
        """
        # Список всех расходов
        self.expenses = []

        # Массив дневных сумм
        self.daily_totals = [0] * 32

        # Массив префиксных сумм
        self.prefix_sums = [0] * 32

        # Стек отмены
        self.undo_stack = Stack()

        # Бинарное дерево поиска для хранения расходов
        self.expense_tree = ExpenseTree()

    def add_expense(self, day, amount, category):
        """
        Метод добавляет расход в программу

        Принимает в качестве аргументов:
        day - день месяца от 1 до 31
        amount - сумма расхода
        category - категория расхода

        Возвращает:
        Созданный объект Expense
        """
        # Проверяем номер дня на попадание в диапазон месяца
        if not 1 <= day <= 31:
            raise ValueError("День должен быть числом от 1 до 31.")

        # ПроверяемЮ что сумма расхода не отрицательная
        if amount <= 0:
            raise ValueError("Сумма расхода должна быть больше 0.")

        # Проверяем, что категория не пустая
        if category == "":
            raise ValueError("Категория не может быть пустой.")

        # Создаем объект расхода
        expense = Expense(day, amount, category)

        # Добавляем расход в список трат и стек отмены
        self.expenses.append(expense)
        self.undo_stack.push(expense)

        # После добавления расхода нужно обновить все структуры
        self.rebuild_data()

        # Возвращаем последний расход, чтобы вывести его юзеру
        return expense

    def get_tree_expenses(self):
        """
        Метод возвращает расходы из дерева в порядке
        возрастания дней.
        """
        # inorder_traversal() выполняет симметричный обход дерева
        return self.expense_tree.inorder_traversal()
    
    

