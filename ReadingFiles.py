file = open("example1.txt", "r")

outfile = "I added this line"

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file.close()


#If opening a file in write mode, it will ALWAYS
# ALWAYS delete existing content. 
# Open file in read mode, copy contents, close file
# open file in writing mode and paste contents before
# adding what youneed to add.

file = open("example1.txt", "w")
file.write(outfile)
file.close()

# Version 2

file1 = open("example.txt", "r")
var1 = file1.readlines()
file1.close()

file1 = open("example.txt", "w")
for i in var1:
        file1.write(i)
input_ =  f"\n2"
file1.write(input_)
file.close

#The outfile is the variable in which we are 
# storing the data we wish to keep.
#The readline in the else statement skips the 
#lines which are odd.