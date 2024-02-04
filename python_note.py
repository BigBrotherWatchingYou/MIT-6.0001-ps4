"""which of this create a car?"""
class car(object):
    def _init_(self,w,d):
        self.wheels = w
        self.doors = d
mycar = car(mycar,2,4)
# this one in wrong: car(mycar,4,2)     car is just like a "kx+b", and mycar= y----y=kx+b

# getters and setters
class Animal(object):
    def _init_(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        #tell the age
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