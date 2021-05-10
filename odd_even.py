import random 
def oddeven(a, b):
    c = a+b 
    if (d==0):
        if (c%2==0):
            return ("YOU WIN!")   
        else:
            return ("YOU LOSE!")

    if (d==1):                          
        if (c%2!=0):
            return ("YOU WIN!")
        else:
            return ("YOU LOSE!")

    else:
        return none      
     

d = int(input("CHOOSE 0 FOR EVEN AND 1 FOR ODD : "))
a = random.randint(1, 10**100)
b = int(input("YOUR TURN TO CHOOSE A NUMBER : ")) 

print(oddeven(a,b))