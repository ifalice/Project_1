class Person:
    
    def __init__(self, name):
        self.__name = name

    @property
    def call(self):
        return self.__name

    @call.setter
    def call(self, new_name):
        self.name = new_name

    @call.deleter
    def call(self):
        del self.name

a = Person("Yura")
print(a.call)
b = Person("Misha")

        