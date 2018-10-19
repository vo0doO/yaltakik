import os
import re

SIMFER_TEXT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/simferopol"
SIMFER_TEXT_FINAL_PATH = os.path.dirname(os.path.abspath(__file__)) + "/simferopol-final"



# ЧИТАТЕЛЬ ИСХОДНОГО ТЕКСТА
def text_reader(file):
    with open(file, "r") as text:
        txt = text.read().replace("+", "").replace("-", "").replace("\n", "").replace("", "").replace("(", "").replace(")", "").replace(" ", "")
    return txt

# ЗАПИСЫВАЕТ ОБРАБОТАННЫЙ ТЕКСТ
def text_writer(file, text_to_write):
    with open(file, "w") as text:
        text.write(final_text)

# ОБРАБОТАННЫЙ ТЕКСТ
final_text = text_reader(SIMFER_TEXT_PATH)

# ПИШЕМ ТЕКСТ В ФАЙЛ
# text_writer(SIMFER_TEXT_FINAL_PATH, final_text)


# КОМПИЛИРУЕМ ВЫРАЖЕНИЕ ДЛЯ ПОИСКА
pattern = re.compile(r"\d{11,}")

# ВЫПОЛНЯЕМ ПОИСК В ТЕКСТЕ И ЗАПИСЫВАЕМ РЕЗУЛЬТАТ В ПЕРЕМЕННУЮ
result = pattern.findall(final_text)
print(f"Всего телефонов: {len(result)}")
# ПРЕОБРАЗУЕМ РЕЗУЛЬТАТ В МНОЖЕСТВО
result = set(result)

# ОБРАТНОЕ ПРЕОБРАЗОВАНИЕ МНОЖЕСТВА В СПИСОК
result = list(result)
print(f"Разных телефонов: {len(result)}")

# ПЕЧАТАЕМ РЕЗУЛЬТАТ
count = 0
max_index = len(result) - 1
while count <= max_index:
    print(result[count])
    count += 1

# ЗАПИСЫВАТЕЛЬ МНОЖЕСТВА ПО СТРОКАМ В НОВЫЙ ФАЙЛ
def tel_set_writer(tels, path):
    with open(path, 'w') as tel_set:
        for tel in tels:
            tel_set.writelines(tel.replace(" ", "") + '\n')


# ПИШЕМ МНОЖЕСТВО ПО СТРОЧНО В ФАЙЛ
tel_set_writer(result, "/home/node/PycharmProjects/yaltakik/simferopol-sevastopol-set.txt")