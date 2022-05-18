from abc import ABC, abstractmethod

# We are going to create some classes. The 
# superclass is going to be Bird.
class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False


class Owl(Bird):
    def reproduce(self):
        self.babies += 6
    def eat(self):
        return "Peck peck"
# So we have used Polymorphism to override the 
# reproduce method, Abstraction with the eat 
# method and Inheritance in this child class.


# Now we will add another subclass.
class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1
#For this subclass we have used Polymorphism
#  to override the reproduce method and Fly 
# and extinct variables, Encapsulation to 
# keep the babies variable from being directly 
# accessed as well as Inheritance again to 
# create a child class of Bird.