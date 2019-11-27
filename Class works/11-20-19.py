# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]


#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])


# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)  #super().__init__(3) 

#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)



# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,2)

#     def findArea(self):
#         a, b = self.sides
#         area = a * b
#         print('The area of rectangle is {}'.format(area))

# n = Rectangle()
# n.inputSides()
# n.findArea()



# 1.  Створити клас машина з атрибутами name,  make, model та методами start та stop,
#  які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.

# class Car:
#     def __init__(self,name,make,model):
#         self.name = name
#         self.make = make
#         self.model = model
    
#     def start(self):
#         print('{} is start'.format(self.name))


#     def stop(self):
#         print('{} is stop'.format(self.name))


# n = Car('Daewoo', 'ZAZ', 'Lanos')
# n.start()
# n.stop()




# 2.  Створити клас особа,  в якому конструктор встановлює ім’я,
#  а метод info виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”,
#   а також створити клас автомобіль,  в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
# {ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def info(self):
#         print('Hello, my name is {}'.format(self.name))

# class Car:
#     def __init__(self, name):
#         self.name = name
    
#     def move(self, speed):
#         print('{} moves at the speed {} km/h'.format(self.name, speed))
        
# name = Person('Python')
# name.info()

# car = Car('Supra')
# car.move(220)


# 3.  Створити клас особа,  в якому конструктор встановлює ім’я, вік. 
# Використати в цьому класі геттери та сеттери, а також створити метод info,
# який виводить інформацію про ім’я та вік особи. А тоді створити клас працівник,
# який наслідується від класу особи і містить метод details, який на вхід отримує 
# параметр про компанію, в якій працює працівник і цей метод виводить інформацію про те,
# що працівник з таким то іменем працює в такій то компанії.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age
        
#     def info(self):
#         print('Name: {}. Age: {}.'.format(self.name, self.age))

# class Worker(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def details(self, company):
#         self.company = company
#         print('Worker named {}, work in {} company'.format(self.name, self.company))
        
        
# pers = Worker('Igor Guban', 30)
# pers.info()
# pers.details('LKP LEV')


# 4.  Створити батьківський клас Figure з методами 
# init: ініціалізується колір,
# get_color: повертає колір фігури, 
# info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle,
# Square, які мають інформацію про ширину, висоту фігури,
#  метод square, який знаходить площу фігури.


# class Figure:
#     def __init__(self,color,figure):
#         self.color = color
#         self.figure = figure
        
#     def get_color(self):
#         return self.color
    
#     def info(self):
#         return self.color, self.figure

# class Rectangle(Figure):
#     def __init__(self, height, weight, color, figure):
#         super().__init__(color, figure)
#         self.height = height
#         self.weight = weight
    
#     def square(self):
#         return self.height * self.weight
        
# class Square(Figure):
#     def __init__(self, side, color, figure):
#         super().__init__(color, figure)
#         self.side = side
    
#     def square(self):
#         return self.side * self.side
    
    
    
     
# fig = Figure('red','Recktangle')
# print(fig.get_color())
# print(fig.info())
# sd = Rectangle(2, 11, 'blue', 'Rectangle')
# sd.square()
# md = Square(4, 'green', 'Square')
# md.square