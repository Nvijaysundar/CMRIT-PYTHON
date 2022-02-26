class Student:
    def __init__(self,name,rollno):
        self.name =name
        self.rollno=rollno
    def show(self):
        print(self.name,self.rollno)
    class Mobile:
        def __init__(self):
            self.brand ='Oneplus'
            self.ram=8
            self.cam = '48mp'
s1 = Student('vj',2)
s2 = Student('k',3)
s2.show();
m1 = Student.