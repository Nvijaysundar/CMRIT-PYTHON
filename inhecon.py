class A:
    def __init__(self):
        print("A's Init")
class B:
    def __init__(self):
        print("B Init")
class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("C' INit")

c1 = C()