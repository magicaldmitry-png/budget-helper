class Expense:
    """
    хранит информацию об одном расходе, получается, что
    у расхода есть только три атрибута: день, сумма и категория
    """
    def __init__(self, day, amount, category):
        """
        создаёт объект расхода, принимающий в качестве аргументов:
        день месяца от 1 до 31, сумму расходов и категорию этих расходов
        """
        self.day = day
        self.amount = amount
        self.category = category
    def __str__(self):
        """
        возвращает строку для красивого вывода расхода
        """
        # если сумма целая, то выводим её без лишней части с нулями 
        if self.amount == int(self.amount):
            amount_text = str(int(self.amount))
        else:
            amount_text = str(round(self.amount, 2))
        return f"{self.day} день | {amount_text} руб. | {self.category}"