from abc import ABC,abstractmethod
class animals(ABC):
    def move(self):
        pass
class human(animals):
    def move(self):
        print("i can walk and run")
class snake(animals):
    def move(self):
        print("i can crawl")
class dog(animals):
    def move(self):
        print("i can bark")
class lion(animals):
    def move(self):
        print("i can roar")
R=human()
R.move()
K=snake()
K.move()
R=dog()
R.move()
K=lion()
K.move()
