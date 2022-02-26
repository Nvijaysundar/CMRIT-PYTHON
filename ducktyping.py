class Pycharm:
    def execute(self):
         print("compiling")
         print("running")
class Myeditor:
    def execute(self):
        print("compiling")
        print("running")
        print("Spell check")
class Laptop:
    def code(self,ide):
        ide.execute()
ide = Myeditor()
lap1 = Laptop()
lap1.code(ide)