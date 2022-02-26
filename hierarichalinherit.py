class Parent:
    def fun1(self):
        print("this is parent class")
class  Child1(Parent):
    def fum2(self):
        print("this is child 1 class")
class  Child2(Parent):
    def fum3(self):
        print("this is child 2 class")

o1 = Child1()
o2 = Child2()
o1.fun1()
o1.fum2()
o2.fun1()
o2.fum3()