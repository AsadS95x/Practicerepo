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
    mark = int(input ("What was your mark?" ))
    if mark >= 85: 
        print ("Distinction")
    elif mark <65:
        print ("Fail")
    else:
        print ("Pass!")

def studentnames():
    count = 0
    namelist = []
    while count < 5:
        name = str(input("What is the students name "))
        namelist.append(name)
        print("Student ", namelist[count], " is awesome!")
        count += 1
    print ("Students ",*namelist(), " are all awesome! ")

studentnames()