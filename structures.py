"""
structures.py содержит структуры данных для программы Бюджетный помощник

В модуле реализованы: 

1. Stack - стек для отмены последнего добавленного расхода
2. TreeNode - узел бинарного дерева поиска
3. ExpenseTree - бинарное дерево поиска расходов по дням 
"""

class Stack:
    """
    Стек на основе списка. 
    Применяется для отмены последнего добавленного расхода
    """
    def __init__(self):
        """
        Инициализируем пустой стек
        """
        self.items = []

    def push(self, item):
        """
        Метод добавляет элементы в стек.
        Передаем в качестве аргумента объект, который 
        необходимо добавить
        """
        self.items.append(item)

    def pop(self):
        """
        Метод удаляет и возвращает последний элемент стека.
        Если стек пустой, возвращает None
        """
        if self.is_empty():
            return None
        
        return self.items.pop()
    
    def is_empty(self):
        """
        Метод проверяет, пусть ли стек.
        Возвращает True, если стек пустой, 
        или False, если нет. 
        """
        return len(self.items) == 0 
    
    def clear(self):
        """
        Метод очищает стек ото всех элементов
        """
        self.items.clear()

class TreeNode:
    """
    Узел бинарного дерева поиска
    Каждый узел хранит день месяца и список расходов за этот день, поэтому
    если за один день было несколько расходов, то они лежат в одном узле.
    """
    def __init__ (self, expense):
        """
        Метод создает узел дерева, принимая в качестве аргумента 
        expense - объект расхода с полями day, amount, category.
        """
        self.day = expense.day
        self.expenses = [expense]
        self.left = None
        self.right = None

class ExpenseTree:
    """
    Бинарное дерево поиска для хранения расходов по дням
    Ключом дерева является номер дня. Расходы с меньшим днем идут в левое поддерево, 
    с большим - в правое, а если номер совпал, то расход добавляется в список текущего дня.
    """
    def __init__(self):
        """Инициализирует пустое дерево"""
        self.root = None
    
    def insert(self, expense):
        """
        Метод добавляет расход в дерево, принимая аргумент expense -
        объект с полями day, amount, category
        """
        if self.root is None:
            self.root = TreeNode(expense)
        else:
            self.insert_recursive(self.root, expense)

    def insert_recursive(self, node, expense):
        """
        Метод рекурсивно ищет место для нового расхода в дереве. 
        Принимает в качестве аргументов текущий узел node и объект расхода expense.
        """
        # Если номер дня расхода меньше текущего дня, то идем влево
        if expense.day < node.day:
            if node.left is None:
                node.left = TreeNode(expense)
            else:
                self.insert_recursive(node.left, expense)

        # Если номер дня расхода больше текущего дня, то идем вправо
        elif expense.day > node.day:
            if node.right is None:
                node.right = TreeNode(expense)
            else:
                self.insert_recursive(node.right, expense)
        # Если номер дня расхода равен текущему и он не пуст, 
        # то добавляем расход в список
        else:
            node.expenses.append(expense)

    def inorder_traversal(self):
        """
        Метод возвращает расходы в порядке возрастания дней с использованием
        симметричного обхода дерева.
        """
        result = []
        self.inorder_recursive(self.root, result)
        return result

    def inorder_recursive(self, node, result):
        """
        Метод рекурсивно симметрично обходит дерево (в порядке возрастания дней)
        Принимает текущий узел и список расходов
        """
        if node is None:
            return

        self.inorder_recursive(node.left, result)

        for expense in node.expenses:
            result.append(expense)

        self.inorder_recursive(node.right, result)

    def clear(self):
        """Метод очищает дерево"""
        self.root = None