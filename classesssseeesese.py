class myclass:
    __privateVar  =27;
    def __privmeth(self):
        print("im inside class myclass")
    def hello(self):
        print("Private variable value:", myclass.__privateVar)
foo = myclass()
foo.hello()
foo.__privmeth
