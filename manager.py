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


def get_all_expenses(self):
        """
        функция возвращает список всех расходов
        """
        return self.expenses
def get_period_sum(self, start_day, end_day):
        """
        функция возвращает сумму расходов за период, перед подсчётом проверяются границы
        периода и сам подсчёт выполняется через массив префиксных сумм
        """
        #проверяем, что начальный и конечный день входят в диапазон 1-31
        if not self._is_valid_day(start_day):
            raise ValueError("Начальный день должен быть числом от 1 до 31")
        if not self._is_valid_day(end_day):
            raise ValueError("Конечный день должен быть числом от 1 до 31")
        #начальный день не может быть больше конечного.
        if start_day > end_day:
            raise ValueError("Начальный день не может быть больше конечного.")
        return get_period_sum(self.prefix_sums, start_day, end_day)
def get_max_expense_day(self):
        """
        функция возвращает день с максимальными расходами в виде кортежа
    из двух значений: номер дня и сумма расходов в этот день
        """
        #если расходов нет, возвращаем 0 и 0
        if not self.has_expenses():
            return 0, 0
        return find_max_expense_day(self.daily_totals)
def get_sorted_categories(self):
        """
        фунция возвращает категории, отсортированные по сумме расходов,
        сначала считаются суммы по категориям, а затем категории сортируются 
        вставками
        """
        #если расходов нет, возвращаем пустой список
        if not self.has_expenses():
            return []
        category_totals = get_category_totals(self.expenses)
        #сортируем категории по сумме расходов
        return insertion_sort_categories(category_totals)
def _is_valid_day(self, day):
        """
        функция проверяет, что день месяца указан правильно и возвращает
        True, если день является числом от 1 до 31
        False в остальных случаях
        """
        if not isinstance(day, int):
            return False
        return 1 <= day <= 31
def _is_valid_amount(self, amount):
        """
        функция проверяет, что сумма расхода указана правильно и возвращает
        True, если сумма является числом больше 0
        False в остальных случаях
        """
        #сумма может быть целым числом или дробным числом.
        if not isinstance(amount, int) and not isinstance(amount, float):
            return False
        return amount > 0
def has_expenses(self):
        """
        функция проверяет, есть ли в программе расходы и возращает
        True, если список расходов не пустой
    False, если расходов нет
        """
        #если длина списка больше 0, значит расходы уже добавлены
        return len(self.expenses) > 0

