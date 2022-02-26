class A:
    def __init__(self):
        print("init  of A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B's Init")
class C(B):
    def __init__(self):
        super().__init__()
        print("C's Constructor")

c1 = C()