################################# Task 1

# num = []
# for rem in range(0,100):
#    if rem%2 == 0:
#        num.append(rem)
# print(num)
    

################################# Task 1.1


# num = []
# count = 0
# while count <= 100:
#    count += 1
#    if count%2 == 0:
#        num.append(count)
# print(num)
    

################################# Task 2


# for num in range(0,100):
#     if num%2 == 0:
#         continue
#     print(num)


################################# Task 2.1    


# for num in range(1,100,2):
#     print(num)


################################# Task 3


# num = (8, 2, 22, 10, 22, 12)
# for a in num:
#     if a%2 != 0:
#         print("List have odd number")
#         break
# else:
#     print("All numbers is even") 


################################# Task 4


# num_list=[0, 23, 122, 855, 2, 32, 46, 100]
# for num in num_list:
#    print(float(num))


################################# Task 5


# n = int(input('Enter number for start: '))
# a , b = 0, 1
# for fib in range(n):
#     print (a)
#     a, b = b, b + a
    

################################# Task 6


# word = ['control', 'folk', 'synth', 'jump']
# for step in word:
#    print(step)


################################# Task 7


# wordlist = ['control', 'folk', 'synth', 'jump']
# for step in wordlist:
#    for char in step:
#        print(char, end = '#')


################################# Task 8


# def simple(num):
#     check = True
#     for a in range(2,num):
#         if num%a == 0:
#             check = False
#             break
#     if check:
#         return print("It's prime number")
#     else:
#         return print("It's complex number")


# simple(int(input("Enter number for check: ")))


################################ Task 9


# from random import random


# num = random()
# print(num)
# print(max(list(str(num))))
    
    
################################ Task 10


# word = input('Enter word for check: ')
# for step in range(len(word)):
#     if word[step] != word[-1 - step]:
#         print ("Isn't palindrom")
#         break
# else:
#     print ("Is palindrom")



       


