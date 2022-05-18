
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
print (dog1.name)
print (dog2.speak())
print (dog2.breed)

class Student():

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_

    def calculate_final(self, mark1, mark2, mark3):
        print (" ")
        print ("***** Exam Results for ", self.name , " from Class ", self.class_, " *****")
        print ("Homework score is ", mark1, "out of 25")
        print ("Assessment score is ", mark2, "out of 50")
        print ("Exam score is ", mark3, "out of 100")
        print (" ")
        finalscore = mark1+mark2+mark3
        finalpercent = (finalscore/175)*100
        print ("Your Final Mark is: ", finalscore,) 
        print (" at ", int(finalpercent),"%")
        return finalpercent

    
student1 = Student("Asad", 23, "Devops")
student2 = Student("Charlie", 36, "Cloud")

student1.calculate_final(21, 43, 67)
