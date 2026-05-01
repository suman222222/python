#a class named student having 4 attributes :name,maths,science,english)
class Student():
    def __init__(self,name,maths,science,english):
        self.name=name#stores name in object
        self.maths=maths
        self.science=science
        self.english=english

    def get_lname(self):#method
        parts= self.name.split()#converts into list
        return parts[-1]
    def get_average(self):
        average=(self.maths +self.science + self.english)/3
        return average

        
S1 = Student("Harry Potter", 80, 80, 80)#s1 is an object
print("Last Name:",S1.get_lname())
print("Average marks:",S1.get_average())
        
