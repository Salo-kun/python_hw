############################### Task 1


# def arithmetic_mean(*arg):
#     return sum(arg)/len(arg)

# print(arithmetic_mean(10, 25, 23 ,11))


############################### Task 2


# def absoluting(num):
#     return num if num >= 0 else num - 2 * num

# print(absoluting(-24))     


############################### Task 3


# def maximizer(a, b):
#     '''This function return maximum of two number'''
#     return max(a,b)


# print(maximizer(20,10))    
# print(maximizer.__doc__)


############################## Task 4


# import math


# def calc_area_rectangle(a, b):
#     return a * b


# def calc_area_triangle(a, b, c):
#     p = (a + b + c) / 2
#     return math.sqrt(p * (p - a) * (p - b) * (p - c))


# def calc_area_circle(r):
#     return math.pi * r ** 2



# choise = int(input(
# '''For calcuclating area, input number of your figure
# 1. Rectangle
# 2. Triangle
# 3. Circle 
# Figure: '''
# ))
# while choise < 1 or choise > 3:
#     choise = int(input('Not correct number. Try again: '))

# if choise == 1:
#     a = float(input('Enter lenght of rectangle first side in meter : '))
#     b = float(input('Enter lenght of rectangle second side in meter: '))
#     print('Area of rectangle is {0:.3f} m^2'.format(calc_area_rectangle(a, b)))
# elif choise == 2:
#     a = float(input('Enter lenght of tiangle first side in meter: '))
#     b = float(input('Enter lenght of tiangle second side in meter: '))
#     c = float(input('Enter lenght of tiangle third side in meter: '))
#     test = (a, b, c)
#     sor = sorted(test)
#     while sor[2] >= sor[0] + sor[1]:
#         print("It's not a triangle. Try again")
#         a = float(input('Enter lenght of tiangle first side in meter: '))
#         b = float(input('Enter lenght of tiangle second side in meter: '))
#         c = float(input('Enter lenght of tiangle third side in meter: '))
#         test = (a, b, c)
#         sor = sorted(test)

#     print('Area of triangle is {0:.3f} m^2'.format(calc_area_triangle(a, b, c)))
# else:
#     r = float(input('Enter radius of circle in meter: '))
#     print('Area of circle is {0:.3f} m^2'.format(calc_area_circle(r)))
