name=input("What is your name? ")
age=input("How old are you? ")
city=input("Where do you live? ")
message_name= 'Hello, {}.'
message_age='Your age is {}.'
message_city='You live in {}.'
print(message_name.format(name), message_age.format(age), message_city.format(city))