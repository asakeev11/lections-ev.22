# with open ('text.txt', 'w+') as file:
#     file.writelines(['1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8', '\n9', '\n10'])
#     for x in file.readlines(9):
#         print(x)

# x = open('text.txt', 'r')
# for line in x.readlines(8):
#     print(line)

# with open('text.txt', 'r') as file:
#     for line in file.readlines(8):
#         print(line)

# with open('text.txt', 'r') as file:
#     print(file.read())

# with open('text.txt', 'w') as file:
#     file.writelines(['1 2 3 4 5 6 7 8 9 10'])

# with open('text.txt', 'w+') as file:
#     file.writelines(['1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8', '\n9', '\n10', '\n11', '\n12', '\n13', '\n14', '\n15'])
# with open('text.txt', 'r') as file:
#     x = file.readlines()
#     print(len(x))

# with open('text.txt', 'r') as file:
#     y = file.readlines()
#     z = list(map(lambda x:int(x), y))
#     max = max(z)
#     min = min(z)
# with open('task5.txt', 'w') as file:
#     file.writelines([f'max_num:{max}\nmin_num:{min}'])
    
# x = 'Hi guys'
# z = len(x.split())
# print(z)

# with open('text.txt', 'r') as file:
#   x = file.readlines()
#   print(f'Количество строк - {len(x)}')
# with open('text.txt', 'r') as file:
#   z = list(filter(lambda x: x.split('\n'), file))
#   for i in range(len(z)):
#     t = z[i].rstrip('\n')
#     dlina_str = (len(t))
#     words = (len(t.split()))
#     print(f'{t} - Количество символов: {dlina_str}, Количество слов: {words}')
  
# with open('text.txt', 'r') as file:
#   x = file.readlines()
#   print(f'Количество строк - {len(x)}')
# with open('text.txt', 'r') as file:
#   for i in file.readlines():
  
#     print(len(i))
    
# with open('text.txt', 'r') as file:
#   x = file.readlines()
#   string = ' '.join(line.strip() for line in x)
#   print(string)


  # with open('text2.txt', 'r') as file:
  # x = file.readlines()
  # for i in range(len(x)):
  #   z = (x[i].rstrip('\n'))
  #   # print(z[-1])
  #   for i in z[-1]:
  #     if int(z[-1]) < 3:
  #       with open('bad.txt', 'a') as file:
  #         file.writelines(z)
# import functools
# x = 12345
# suma = (functools.reduce(lambda a : a, x))
# print(suma)

# with open('text2.txt', 'r') as file:
#   x = file.readlines()
#   for i in range(len(x)):
#     z = (x[i].rstrip('\n'))
#     # print(z[-1])
#     for i in z[-1]:
#       if int(z[-1]) < 3:
#         with open('bad.txt', 'a+') as file:
#           file.writelines((f'{z}\n'))
#     with open('marks.txt', 'a+') as file:
    
#       file.writelines((z[-1].split()))
#     suma = 0
#     with open('marks.txt', 'r') as file:
#       o = file.read()
#   ls = list(o)
#   suma = list(map(int,ls))
#   print(suma)





  # with open('text2.txt', 'r') as file:
  # x = file.readlines()
  # for i in range(len(x)):
  #   z = (x[i].rstrip('\n'))
  #   # print(z[-1])
  #   for i in z[-1]:
  #     if int(z[-1]) < 3:
  #       with open('bad.txt', 'a+') as file:
  #         file.writelines((f'{z}\n'))
  #   with open('marks.txt', 'a+') as file:
    
  #     file.writelines((z[-1].split()))
  #   suma = 0
  #   with open('marks.txt', 'r') as file:
  #     o = file.read()
  # ls = list(o)
  # suma = list(map(int,ls))
  # sm = sum(suma)
  # average = int(sm)/int(len(suma))
  # print(average)
  
#  with open('text2.txt', 'r') as file:
#   x = file.readlines()
#   for i in range(len(x)):
#     z = (x[i].rstrip('\n'))
#     # print(z[-1])
#     for i in z[-1]:
#       if int(z[-1]) < 3:
#         with open('bad.txt', 'w') as file:
#           file.writelines((f'{z}\n'))
#     with open('marks.txt', 'a+') as file:
    
#       file.writelines((z[-1].split()))
#     suma = 0
#     with open('marks.txt', 'r') as file:
#       o = file.read()
#   ls = list(o)
#   suma = list(map(int,ls))
#   sm = sum(suma)
#   average = int(sm)/int(len(suma))
#   print(f'Средний балл класса - {average}')
  

# x = input('Ввод: ').lower()
# if x == 'привет':
#   z = input('Выберите офис:\n1)google_kazakstan\n2)google_paris\n3)google_poland\n4)google_kyrgyzstan\n5)google_san_francisco\n6)google_germany\n7)google_moscow\n8)google_sweden\n')
#   if z == 1:
#     kz = input('Напишите вашу жалобу: ')
#     with open('google_kazakstan.txt', 'w') as file:
#       file.writelines(kz) 

with open('google.kazakstan.txt', 'a+') as file:
  file.writelines('hi')