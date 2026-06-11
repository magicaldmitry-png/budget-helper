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
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0 
    
    def clear(self):
        self.items.clear()

class TreeNode:
    """
    Узел бинарного дерева поиска
    Каждый узел хранит день месяца и список расходов за этот день, поэтому
    если за один день было несколько расходов, то они лежат в одном узле.
    """
    def __init__ (self, expense):
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
        self.root = None
    
    def insert(self, expense):
        if self.root is None:
            self.root = TreeNode(expense)
        else:
            self.insert_recursive(self.root, expense)

    def insert_recursive(self, node, expense):
        if expense.day < node.day:
            if node.left is None:
                node.left = TreeNode(expense)
            else:
                self._insert_recursive(node.left, expense)

        elif expense.day > node.day:
            if node.right is None:
                node.right = TreeNode(expense)
            else:
                self._insert_recursive(node.right, expense)

        else:
            node.expenses.append(expense)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return

        self._inorder_recursive(node.left, result)

        for expense in node.expenses:
            result.append(expense)

        self._inorder_recursive(node.right, result)

    def clear(self):
        self.root = None