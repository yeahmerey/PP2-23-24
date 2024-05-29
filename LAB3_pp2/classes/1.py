class String1:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

a = String1()
a.getString()
a.printString()