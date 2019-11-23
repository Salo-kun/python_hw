def list_animals(animals):
    string = ''
    for i in range(len(animals)):
        string += str(i + 1) + '. ' + animals[i] + '\n'
    return string