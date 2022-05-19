from app import dice
#from random import seed

print (dice(), " ", dice())



#Create a Python file which does the following:
#Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
#Reads and displays the names of the 1st and 4th team in the file.

file = open("teams.txt", "w")
file.write("Rocks\nLakers\nHeat\nCavliers\nWarriors\n")
file.close


#Create a new Python file which does the following:
#Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
#Print out the edited file line by line.

file = open("teams.txt", "r")
var1 = file.readlines()
file.close

file = open("teams.txt", "w")
file.write("We just added a new line\n")
for i in var1:
        file.write(i)
        print(i) # easy method
file.close
#proper method
file = open("teams.txt", "r")
var1 = file.readlines()
file.close
for i in var1:
       print(i)


