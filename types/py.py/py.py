# a = input()
# b = a[::-1]
# if a==b:
#     print('YEs')
# else:
#     print('No')


# str = 'hello world'
# b = str.split(str)


# a = [1,56,78,2,100, 12]
# b = int(a[0]+int(a[1])+int(a[2])+int(a[3])+int(a[4]))
# print (b)

fib1=1
fib2=1

n = input()

i = 0
while i < int(n) - 2:
    fib_sum= fib1+fib2
    fib1=fib2
    fib2=fib_sum
    i = i+1
    
print(fib2)


# for i in range(50):
#     if i % 5:
#         print('Fizz')
#     elif i % 5:
#         print('Bazz')
#     else:
#         print('FillBazz')
