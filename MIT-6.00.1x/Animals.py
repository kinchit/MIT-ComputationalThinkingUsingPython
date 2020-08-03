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

class Cat(Animal):
    def speak(self):
        print("Meow")
    
    def __str__(self):
        return "Cat: " + str(self.name) + ": " + str(self.age)

class Person(Animal):
    def __init__(self,age,name):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends = []
    
    def get_friends(self):
        return self.friends
    
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    
    def speak(self):
        print("Hello")
    
    def __str__(self):
        return "Person: " + str(self.name) + ": " + str(self.age)

Jelly = Cat(1)

print(Jelly)

Jelly.set_name('JellyBelly')

Jelly.get_name()

print(Jelly)

print(Animal.__str__(Jelly))

blob = Animal(2)

Jelly.speak()

#blob.speak() # Throws attribute error as blob is of type animal and superclass has no speak method

