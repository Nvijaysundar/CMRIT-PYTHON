class A:
    def show(self):
        print("On A Show")
class B(A):
    def show(self):
        super().show()
        print("In B bLock")
a1 =B()
a1.show()