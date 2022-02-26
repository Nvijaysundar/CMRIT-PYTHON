class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def show(self):
        print(self.name, self.roll)
    class Mobile:
        def __init__(self):
            self.brand ='Onepuls'
            self.ram = 8
            self.cam= '48mp'
        def show(self):
            print(self.brand,self.ram,self.cam)
s1 = Student('vj',2)
s1.show()
mob1 = Student.Mobile()
mob1.show()
