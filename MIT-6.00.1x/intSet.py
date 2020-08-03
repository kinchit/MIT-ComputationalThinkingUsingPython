class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self,other):
        newVals = intSet()
        if type(self) == type(other):
            if len(self.vals) == 0 and len(other.vals) == 0:
                return newVals
            if len(self.vals) == 0:
                return other.vals
            elif len(other.vals) == 0:
                return self.vals
            else:
                for val in self.vals:
                    if other.member(val):
                        newVals.insert(val)
        return newVals
    
    def __len__(self):
        return len(self.vals)


s1 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(4)
print(s1)
s2 = intSet()
s2.insert(3)
s2.insert(4)
print(s1.intersect(s2))