class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self,newAge):
        self.age = newAge
        
    def set_name(self,newName = ""):
        self.name = newName
    
    def __str__(self):
        return "Animal: " + str(self.name) + ": " + str(self.age)
    
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1 = None, parent2 = None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    
    def get_rid(self):
        return str(self.rid).zfill(3)
    
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
    def __add__(self,other):
        if type(self) == type(other):
            return Rabbit(0,self,other)
    
peter = Rabbit(2)
peter.set_name("Peter")
lopsy = Rabbit(3)
lopsy.set_name("Lopsy")
cotton = Rabbit(1, peter, lopsy)
print(cotton.get_rid())
cotton.set_name("Cottontail")
print(cotton)