# [а-яА-ЯёЁ] - кирилица
# [0-9] или \d - все цифры
# [^0-9] или \D - всё кроме цифр
# [a-z0-9_] или \w

import re

# Пример поиска по тексту
txt = """
    Ауди стоит 1000,
    БМВ стоит 1200,
    VW стоит 900
"""

# Получим список всех чисел из текста

# prices = re.findall(r"\d+",txt)
# print(prices)

# Пример замены подстроки

# regex_rule = re.compile(r"\d+") #создали правило
# print(regex_rule.sub("...",txt))


# Общие примеры

# text = '10 апреля 2025 года!!!'
# # print(re.findall(r'\d{2}',text))
# print(re.findall(r'\W',text))

# Проверка на email
test = "demo@mail.ru"
rule = r"^[\w.-]+@[\w.-]+\.[a-z]{2,5}$"
if re.fullmatch(rule,test):
    print("Email корректный")
else:
    print("email некорректтный")