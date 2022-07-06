# import random

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Dymdama']
# p = 0
# m = 0
# k = 0
# l = 0
# d = 0
# for i in range(0, 100000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p = p + 1 #p += 1 инкремент
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() == 'kuurdak':
#         k +=1
#     elif choice.lower() == 'lagman':
#         l += 1
#     elif choice.lower() == 'dymdama':
#         d += 1
    
# print(f'Plov: {p} \nM       anty: {m} \nKuurdak: {k} \nLagman: {l}')

# dict_ = {'Plov' : p, 'Manty' : m, 'Kuurdak' : k, 'Lagman' : l, 'Dymdama' : d}
# # print(dict_)
# result = sorted(dict_.items(), key = lambda x: x[1])
# winner = result[-1]
# print(f'Победило блюдо {winner[0]}, оно набрало: {winner[1]} баллов')

# lambda x: x[1]
# '''=='''
# def func(x: tuple):
#     return x[1]




# x = {'a':1,'b':2,'c':3}
# for i in x.keys():
#     if x[i] % 2 == 0:
#         x[i] = 1
# print(x)


# def countingValleys(steps, path):
#     x = 8
#     y = 'DDUUDDUUDUUUD'
#     V = 0
#     L = 0
#     for i in y:
#         global y
#         if 'D' in i:
#             V += 1
#         elif 'U' in i:
#             L += 1
# print(V, L)


# def countingValleys(steps, path):
#     dolina = 0
#     sea_level = 0
#     for x in path:
#         if x == 'U':
#             sea_level += 1
#             if sea_level == 0:
#                 dolina += 1
#         elif x == 'D':
#             sea_level -= 1
#     return dolina
# print(countingValleys(100, 'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'))
# names = ['Talgat', 'Beka', 'Aiba', 'Mura', 'Aibekk']
# import functools
# z = functools.reduce(lambda x, y: x if len(x) >= len(y) else y, names)
# print(z)



# a = ['1', '2']
# b = list(map(int, a))
# print(b)




print(divmod(3,2))
