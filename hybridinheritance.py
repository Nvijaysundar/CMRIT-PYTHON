class Father:
    def property1(self):
        print('this is father property')
class Mother(Father):
    def property2(self):
        print('this is mother property')
class Husband:
    def property3(self):
        print('this is husband property')
class Wife(Mother, Husband):
    def propertry4(self):
        print("this is my property and other property")

w1 = Wife()
w1.property1()
f1= Father()
m1= Mother()
h1 = Husband()
h1.property3()
m1.property2()


