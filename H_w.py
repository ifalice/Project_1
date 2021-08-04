class Person:
    
    def __init__(self, name):
        self.__name = name

    @property
    def call(self):
        return self.__name

a = Person("Yura")
print(a.call)


        