def ehh(reply):
    if reply.upper() == 'Y':
        print ( "Wohooo!")
    elif reply.upper() == 'N' :
        print ("Goddaaamit!") 
        op()
    

def op():
    print ("Hi i don't know you" )
    fname = input ("Whats your name? :")
    sname = input ("And your surname too :" )
    print ("You have told me your name is " + fname + " " +  sname)
    print (ehh(input ("Is this correct? Y/N ")))

def dev_money():
    if devs_money > 10 and dev_can_play_smash:
        print("Dev enters a smash tournament!")
    elif devs_money < 10 and dev_can_play_smash:
      print("Dev is too poor to enter")
    else:
     print("Dev just can't play smash")

def class_score():
    '''
    Asks for an input from the user as a mark.
    If the mark is greater that 85 print "Distinction"
    If the mark is between 65 and 85 print "Pass"
    Anything else print "Fail"
    '''
    mark = int(input ("What was your mark?" ))
    if mark >= 85: 
        print ("Distinction")
    elif mark <65:
        print ("Fail")
    else:
        print ("Pass!")

def studentnames():
    '''
    Write a while loop which asks for the names of 5 
    people, and for each person prints their name 
    followed by the text "is awesome!"
    '''
    count = 0
    namelist = []
    while count < 5:
        name = str(input("What is the students name "))
        namelist.append(name)
        print("Student ", namelist[count], " is awesome!")
        count += 1
    print ("Students ",*namelist(), " are all awesome! ")

def class_ranker():
    '''
The program should take the students name, 
homework score (/25), assessment score (/50) 
and final exam score (/100) as inputs, and 
output their name and final ICT grade as a 
percentage.

Reminder: any inputs and prints should not 
be included inside the function definition,
and should strictly be done outside.

Stretch goal: Include grade boundaries such 
that the program also outputs a grade for 
the student (A, B, etc.)
    '''
    slist = []
    hwscore = []
    asscore = []
    examscore = []

    for i in range(5):
        sname = str(input("What the students name? "))
        slist.append(sname)
        hwscore.append(int(input(" What was your homework score? ")))
        asscore.append(int(input(" What was your assesment score? ")))
        examscore.append(int(input(" What was your exam score? ")))
        print (" ")


    for i in range( len(slist) ):
        print (" ")
        print (" *****Exam Results for ", slist[i], " *****")
        print ("Homework score is ", hwscore[i], "out of 25")
        print ("Assessment score is ", asscore[i], "out of 50")
        print ("Exam score is ", examscore[i], "out of 100")
        print (" ")
        finalscore = hwscore[i]+asscore[i]+examscore[i]
        print (slist[i], "your Final Mark is: ", finalscore,) 
        print (" at ", (int(finalscore)/175),"%")

    

def finalmark(student, homework, assement, exam):
    for i in len(student):
        print (i)
        print ("Homework Score:", homework[i]) 

class_ranker()


    

   
