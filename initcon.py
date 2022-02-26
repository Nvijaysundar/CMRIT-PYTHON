class A:
    def __init__(self):
        print("init of A")
class B():
    def __init__(self):
        print("init of B")
    def show(self):
        print("Show of B")
class C(B,A):
    def __init__(self):
        print("Init of c")
        super().__init__()
c1 = C()
c1.show()