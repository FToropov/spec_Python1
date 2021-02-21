""" 7. В банкомате есть купюры 5000, 2000, 1000, 500, 100 рублей.
    Количество купюр каждого номинала ограничено.
    Каждый кортеж в списке - это номинал и количество.
    Напишите функцию, которая будет рассчитывать количество купюр,
    которыми можно будет выдать запрошенную пользователем сумму и
    возвращать ее в виде словаря, ключами в котором будут номиналы банкнот.
    Если пользователь запросил некорректную сумму(больше, чем можно выдать,
    нужно вывести дружественное сообщение об ошибке.
    Результат работы функции вывести на экран(номинал и количество купюр)
"""
nominals = ((5000, 5), (2000, 10), (1000, 15), (500, 20), (100, 50))
bankomat = dict(nominals)

def calc_banknotes(amount):
    # ваш код здесь
    return {}


assert total_sum == sum([banknote * count for banknote, count in nominals])