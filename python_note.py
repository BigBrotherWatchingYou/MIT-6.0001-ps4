
# this one in wrong: car(mycar,4,2)     car is just like a "kx+b", and mycar= y----y=kx+b

# getters and setters
class Animal(object):
    def _init_(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        #tell the age
        # Remember there should be a (self)
        return self.age
    def set_age(self, newage):
        #reset the age
        self.age = newage
    def set_name(self, newname=""):
        #set name
        self.name = newname
   
    def _str_(self):
        #turn it into str
        return "animal:"+str(self.name)+"age:"+str(self.age)
    
    # how it works:  
    a = Animal(lion)
    a.set_age(55)
    
    # Inherits from Animal
    class Dog(Animal):
        def speak(self):
          print("Ruff Ruff")
    d = Dog(7)
    d.set_name("Ruffles")
    d.speak()

    # timing a programm
    # use the time module
    import time
