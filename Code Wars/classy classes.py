class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        
    @property
    def info(self):
        return "{}s age is {}".format(self.name, self.age)