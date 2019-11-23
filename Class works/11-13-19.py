# import pyowm

# owm = pyowm.OWM('747e0b601ab68259ae79fec77ba09f68') 

# observation = owm.weather_at_place(input('Enter your city: '))
# w = observation.get_weather()
# wind = w.get_wind()['speed']
# temp = w.get_temperature('celsius')['temp']
# hum = w.get_humidity()
# print('Weather {}, temp: {} wind: {}, humidity: {}.'.format(w, temp, wind, hum))               
###################################### Task 2

# from random import randint


# num = randint(0,100)
# shot = int(input('''You must guess a number in range from 0 to 100
# Enter your choise: '''))
# while shot != num:
#     if shot < num: 
#       shot = int(input('Enter bigger: '))
#     elif shot > num: 
#       shot = int(input('Enter lesser: '))

# print('You win!!!')

####################################
# from math import pow
# from math import pi


# def calc_area_rectangle(a, b):
#     return a * b


# def calc_area_triangle(a, h):
#     return 0.5 * h * a


# def calc_area_circle(r):
#     return pi * pow(r, 2)


# a = float(input('Enter a side lenght of rectangle in meter: '))
# b = float(input('Enter b side lenght of rectangle in meter: '))
# ta = float(input('Enter a side lenght of triangle in meter: '))
# h = float(input('Enter height of triangle in meter: '))
# r = float(input('Enter radius of circle in meter: '))

# print('Area of rectangle is {0:.3f} m^2'.format(calc_area_rectangle(a, b)))
# print('Area of triangle is {0:.3f} m^2'.format(calc_area_triangle(ta, h)))
# print('Area of circle is {0:.3f} m^2'.format(calc_area_circle(r)))
