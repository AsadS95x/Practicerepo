
class Dog():
    
    def __init__(self, breed, name, age=0):
        self.breed = breed
        self.name = name
        self.age = age

    def speak(self):
     return self.name



dog1 =Dog("Pug", "Tim")
dog2 =Dog("Lab", "Fido", 7)

print (dog1.speak())
print (dog2.speak())
    