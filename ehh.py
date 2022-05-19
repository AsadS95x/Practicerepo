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

op()