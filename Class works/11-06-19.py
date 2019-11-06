########################## Task 1


# n = int(input('Enter lenght of list: '))
# lst = []
# for i in range (n):
#     lst.append(int(input('Enter numer: ')))

# print('Maximum: {}. Minimum: {}'.format(max(lst),min(lst)))


########################### Task 1.1


# lst = [int(input('Enter num: ')) for i in range(int(input('Enter lenght of list: ')))]
# print('Maximum: {}. Minimum: {}'.format(max(lst),min(lst)))


########################### Task 2


# lst = []
# lst2 = []
# lst3 = []
# for a in range (1,10):
#     if a%2 == 0:
#         lst.append(a)
#     elif a%3 == 0:
#         lst2.append(a)
#     else:
#         lst3.append(a)
# print(lst)
# print(lst2)
# print(lst3)


############################ Task 2.1


# lst = [a for a in range(1,10) if a%2 == 0]
# lst2 =[a for a in range(1,10) if a%3 == 0]
# lst3 =[a for a in range(1,10) if a%3 != 0 and a%2 != 0]
# print(lst)
# print(lst2)
# print(lst3)

############################ Task 3


# num = int(input('Enter number: '))
# while num < 1:
#   num = int(input('Try again: '))
# a = 1
# for i in range (1,num+1):
#   a *= i
# print(a)


############################ Task 4


# login = input('Enter login: ')
# while (login != 'First'):
#     login = input("Doesn't correct, try again: ")
# print('Hello, {}!'.format(login))


############################ Task 5


# lst = [int(input('Enter num: ')) for i in range(int(input('Enter lenght of list: ')))]
# check = lst[1]
# step = 1
# while check > 1: 
#     check = lst[step]
#     step += 1

# print('Negative or zero in list: {}'.format(check))


############################# Task 6




                

