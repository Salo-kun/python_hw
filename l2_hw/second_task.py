num = input('Enter four digit number: ')

while (len(num) != 4 or num.isdigit() == False):
    num = input("It's not number, or number of digit is not four. Try again: ")


num_mult = str(tuple(num))
num_mult = num_mult.replace("'","")
num_mult = num_mult.replace(',','*')
print('Multiplication of numbers:', eval(num_mult))

print('Revers of numbers:', num[-1] + num[-2] + num[-3] + num[-4])

num_sort = list(num.sort())
print ('Sroted list of numbers: {}{}{}{}'.format(num_sort[0],num_sort[1], num_sort[2], num_sort[3]))
