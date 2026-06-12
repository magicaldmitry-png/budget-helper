"""
в модуле реализованы:
1. построение массива дневных расходов
2. построение массива префиксных сумм
3. подсчёт суммы расходов за период
4. линейный поиск дня с максимальными расходами
5. подсчёт расходов по категориям
6. сортировка категорий вставками
"""
def build_daily_totals(expenses):
    """
    создаёт массив сумм расходов по дням месяца, индекс 0 не 
    используем, чтобы номер дня совпадал с индексом, функция принимает
    список всех расходов и возвращет список с суммами доходов 
    по дням 
    """
    #создаём список на 32 элемента
    daily_totals = [0] * 32
    #проходим по всем расходам и добавляем сумму к нужному дню
    for expense in expenses:
        daily_totals[expense.day] += expense.amount
    return daily_totals

def build_prefix_sums(daily_totals):
    """
    функция строит массив префиксных сумм, то есть префиксная сумма на день
    i - это сумма всех расходов с 1 дня по день i включительно
    """
    #создаём список такой же длины, как daily_totals.
    prefix_sums = [0] * len(daily_totals)
    for day in range(1, len(daily_totals)):
    #текущая префиксная сумма равна прошлой префиксной сумме
        prefix_sums[day] = prefix_sums[day - 1] + daily_totals[day]
    return prefix_sums

def get_period_sum(prefix_sums, start_day, end_day):
    """
    функция возвращает сумму расходов за выбранный период, она принмает
    список префиксных сумм, начальный день периода и конечный день
    """
    #из суммы с 1 дня по конечный вычитаем сумму до start_day, чтобы получить промежуток
    return prefix_sums[end_day] - prefix_sums[start_day - 1]

def find_max_expense_day(daily_totals):
    """
    функция находит день с максимальной суммой расходов линейным поиском и
    возвращает кортеж из двух значений: номер дня и сумма расходов в этот день
    """
    #сначала считаем, что максимальные расходы были в 1 день
    max_day = 1
    max_amount = daily_totals[1]
    #проходим по дням со 2 по 31
    for day in range(2, len(daily_totals)):
        if daily_totals[day] > max_amount:
            max_amount = daily_totals[day]
            max_day = day
    return max_day, max_amount

def get_category_totals(expenses):
    """
    функция считает общую сумму расходов по каждой категории, где
    ключ это категории , а значения это сумма расходов
    """
    category_totals = {}
    #проходим по каждому расходу из списка расходов.
    for expense in expenses:
        if expense.category not in category_totals:
            category_totals[expense.category] = 0
        category_totals[expense.category] += expense.amount
    return category_totals

def insertion_sort_categories(category_totals):
    """
    функция сортирует категории по сумме расходов сортировкой вставками
    категории сортируются по убыванию суммы, чтобы самые большие расходы отображались первыми
    """
    categories = []
    for category, amount in category_totals.items():
        categories.append([category, amount])
    #начинаем со второго элемента, потому что первый уже считается частью спискас
    for i in range(1, len(categories)):
        current_category = categories[i]
        j = i - 1
    #двигаем элементы вправо, пока они меньше текущего
        while j >= 0 and categories[j][1] < current_category[1]:
            categories[j + 1] = categories[j]
            j -= 1
    #ставим текущую категорию на правильное место
        categories[j + 1] = current_category
    return categories
