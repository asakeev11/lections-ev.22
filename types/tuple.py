#Tuple - это структура данных индексируемый, неизменяемый, упорядоченный
# string = str('hello AttackPython')
# string2 = "hello world"
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set1 = {1,2}
# dict1 = {"key":"value"}

# tuple1 = (1,2,3)
# print(type(tuple1)) # -> tuple class

# tuple1 = 1,2
# tuple1[0]=3#error!!!

# print(tuple1[0])

# print(tuple1[0])
# print(type(tuple1))

# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(0,3,2))
# print(tuple4)


# emails = ("Python@gmail.com", "Tima@gmail.com",3,5,["potato",'arbuz','apple'])
# # print(type(emails[-1]))
# last_object = emails[-1] #list
# last_object.append('tomato')
# print(len(emails))

# print(dir(tuple))
# print('*')
# print(dir(list))


# tuple_sequance_first = (2,2,3,4)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first
# print(tuple_sequance)
# indx = tuple_sequance.index(3)
# print(tuple_sequance[indx])

# for value in tuple_sequance:
#     print(value)
# names = ("Talgat","Tima","Aidana","Bermet","ermek")

# names_enter = ['Bermet','Ermek']

# for name in names:
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!!')
#     else:
#         print(f"{name} go home!!!")



# print(len(name))
# print(names[0] + ' Hello')

# first_step_names = []
# names = input('Write the name: ').split(" ")

# for name in names:
#     if len(name) > 4:
#         first_step_names.append(name)
    
# print(first_step_names) 
# print('start for') 
# for i in range (10):
#     print(i)
# print('stop for')

# while 3 > 2:
#     print(f' {i}i work')
#     i +=1
# i = 0
# num = 3
# while num > i:
#     print('Hi')
#     i += 1

# import math
# print(dir(math))

# x = []
# y = (input('Введите что нибудь: ')).split( )
# for i in y:
#     x.append(i)
# print(x)


# a = [1,2,3]
# if a[2]<3:
#     print(a[a[1]])
# else:
#     print(a[1])

# print(7//-3)

# while 1 > 0:
#     x = int(input('Введите число: '))
#     if x % 4 == 0 and x % 100 != 0:
#         print('YES')
#     else:
#         print('NO')


# x = (1,2,2,3,4,5,6)
# print(x.index(2))

# x = 1,'d',7.0,[1,2],{1:'k'},True,None,{1,2,3}
# print(x)

# x = (1,[1,2,3])
# x[1][2] = 4
# print(x)

x = (1,2,3,4)
for i in x:
    print(i)