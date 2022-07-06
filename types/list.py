# list()(список, массив) - это изменяемый, последовательный тип данных, который из себя представляет коллекцию каких  либо объектов.
# my_list = [1,'string', False, None,[1,2,3]]
# print(my_list)
# print(type(my_list))

# 1. -> list(<iterable>)
# my_list = list('Hello world')
# print(my_list)
# tuple_ = ('banana', 'apple','cherry')
# print(tuple_)
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))


# 2. range() -> Возвращает последовательность элементов(числа)
# a = list(range(0,100,2))
# print(a)

# 3. -> []

# my_list = [1,23,242,242]
# print(my_list)
# print(type(my_list))

# print(dir(list))

# append(element) - Добавляет element в конец списка
# list_ = [1,2,3]
# print(list_)
# list_.append(5)
# list_.append([1,2,3])
# print(list_)

# extend(element[iterable]) ->  расширяет список добавляя element в конец.
# list_=[1,2,3]
# list_.extend([1,2,3])
# print(list_)

# insert(<index>,<element>) - добавляет element по указанному index
# list_ = ['string', 2 , 3, False]
# list_.insert(1, [1,2,3,None])
# list_.insert(2,1)
# print(list_)
# print(list_[5])
# print(list_[1][3])
# print(list_[2:5])
# """
# print(len(list_))

# index(element, [start],[end]) - возвращает индекс elementa
# ls = [1,2,33,3,4,5,5,7,2, 'Hello']
# print(ls.index(5, 6))
# if 'Hello' in ls:
#     print('"Hello" is in list:', ls.index("Hello") )

# count(element)-> Возвращает количество вхождений element в списке
# ls= [1,2,3,4,5,5,5,5,1]
# result  = ls.count(5)
# print(result)

# remove(element) - удаляет element, но если такого элемента нет в списке, то выводит ошибку
# pop([index]) - удаляет и возвращает элемент по index, но если index не указан, то удаляет последний элемент
# list_ = [5,1,2,3,4,5]
# list_.remove(5)
# list_.remove(5)
# deleted = list_.pop(1)
# d = list_.remove(4)
# print(list_)
# print(deleted)
# print(d)

# sort([reverse=True/False], [key=<>]) -> сортирует список.Если в аргументах передан reverse=True то список будет отсортирован в убывающем порядке. 
# ls = [5,0,-2,-101,102,23,1]
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls = ['hello','john','London','a']
# ls.sort(reverse=True,key=len)
# print(ls)

# ls = [1, 'h', 3] #изменение списка
# ls[1]=2
# print(ls)
# del ls[-1] #удаление
# print(ls)

# print(dir(list))

# ls = [4,2,5,3,2,4,5,3,]
# ls1 = [2,3,9,7,5,43,66,54]
# ls.extend(ls1) - узнает сумму чисел списка
# x=sum(ls)
# print(x)

# print(dir(tuple))

# x = ['Abracadabra'] 
# b = x[0]
# c =(len(b)//2)+(len(b)%2)
# d = b[c:]+b[:c]
# print(d)

# ls = [1,2,3,4,5]
# print(ls[::-1])
# ls = ['hi', 'Tala']
# print(' '.join(ls))







