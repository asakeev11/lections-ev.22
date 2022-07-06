
# name = input('Enter your name:')
# last_name = input ('Enter your last name:')
# print('Hi, ms/mrs', name ,last_name)


# a = '5'
# print(int(a))


# ls = []
# for i in range(0,200,2):
#     ls.append(i)
#     print(ls)


# ls = []
# for i in range (0,200):
#     if i % 3 == 0 and i % 2 == 0:
#         z = ls.append(i)
# print(ls)


# ls = []
# for i in range(0,101):
#     if i % 2 == 0:
#         ls.append(i**2)
#     elif i % 2 != 0:
#         ls.append(i)
# print(ls)
    

import random
list1 = list(range(0,50))
set1 = {x for x in random.sample(list1, 10)}
set2 = {x for x in random.sample(list1, 10)}
print(set1)
print(set2)
new_set = set1.union(set2)
print(new_set)

if len(new_set) < 20:
  print(f'В этом сете было {20-len(new_set)} повторения, его длинна составляет {len(new_set)}')
else:
  print('Ваше объедененное множество было уникальным')