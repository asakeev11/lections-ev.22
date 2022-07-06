# Методы строк
# dir() - Функция которая вытаскивает методы типов данных
# print(dir(str))
# '<соединитель>' .join(<массив который нужно соединить>) - Соединяет массив из строк по соединителю в одну строку
# ls = ['Milk', 'Bread','Water','Apple']
# joined = ' '.join(ls)
# print(joined)
#  split(разделитель) -> Дробит строку по разделителю и возвращает тип данных list
# text = 'Milk.Bread.Water.Apple'
# splited = text.split('.')
# print(splited)
# joined = ', '.join(splited)
# print(joined)
#replace (<old value>, <new value>,[count]) -> Меняет в строке значение old на new value, если вы укажете count,то он заменит count раз

# text = 'ha ha ha ha'
# result = text.replace('ha', 'la')
# print(result)
# print(text)

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip() - В конце удаляет
# lstrip() - В начале удаляет

# text = input('Введите ФИО: ')
# result = text.lstrip()
# print(text.strip())
# print(result)

# count ('<symbol>') -> считает количество вхождений <symbol> в строку

# text = 'Hello world! I\'m from Earth!'
# result = text.count('l')
# print(result)

#index ('<value>', [start], [end]) -> выводит индекс значения value в нашей строке.
# text = 'Hello world! THis is Makers!'
# result = text.index('',12)
# print(result)
# print(len(text))
# print(text.find('H'))