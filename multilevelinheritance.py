class A:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class B(A):
    def feature3(self):
        print("feature 3working")
    def feature4(self):
        print("feature 4working")
class C(B):
    def feature5(self):
        print("feature 5working")
    def feature6(self):
        print("feature 6working")
a1 = A()
b1=B()
c1=C()
a1.feature2()
c1.feature4()
b1.feature1()
