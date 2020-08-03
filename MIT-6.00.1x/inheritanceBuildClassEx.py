import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def get_lastName(self):
        '''Returns last name of the person '''
        return self.lastName
    
    def __str__(self):
        '''Returns Full Name of the person'''
        return self.name
    
    def set_birthday(self, month, day, year):
        '''Sets persons birthday'''
        self.birthday = (datetime.date(year,month,day))
        
    def get_age(self):
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self,other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

class MITPerson(Person):
    nextIdNum = 0
    
    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def get_idNum(self):
        return self.IdNum
    
    def __lt__(self,other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.name + " says: " + utterance)

class Student(MITPerson):
    pass

class Grad(Student):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self.name)
        self.year = classYear
    
    def get_year(self):
        return self.year
    
    def speak(self,utterance):
        return MITPerson.speak(self, "Yo Bro" + utterance)
    
def isStudent(obj):
    return isinstance(obj,Student)

# p1 = Person("Mark Zukerburg")
# p1.set_birthday(5,14,84)
# p2 = Person("Drew Hudson")
# p2.set_birthday(3,4,83)
# p3 = Person("Kinchit Raja")
# p3.set_birthday(4,15,86)
# print(p1.get_age())
# 
# PersonList = [p1, p2, p3]
# 
# for e in PersonList:
#     print(e.name)
#     
# PersonList.sort()
# print("----")
# for e in PersonList:
#     print(e.name)

m3 = MITPerson("Mark Zukerburg")
Person.set_birthday(m3,5,14,84)
m2 = MITPerson("Drew Hudson")
Person.set_birthday(m2,3,4,83)
m1 = MITPerson("Kinchit Raja")
Person.set_birthday(m1,4,15,86)

MITPersonList = [m1,m2,m3]

for e in MITPersonList:
    print(e)

MITPersonList.sort()
print("----")
for e in MITPersonList:
    print(e)