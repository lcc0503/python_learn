import random
#loops
#while #for
#start condition
#while


num2=0
nu=(random.randint(1, 999999))
running=True
while running==True:
    num=int(input("Password "))
    if num>nu:
        print("Lower ")
        num2=num2+1
    elif num<nu:
        print("Greater ")
        num2=num2+1
    elif num==nu:
        print("Correct! ")
        num2=num2+1
        running=False
print("Code Cracked.",nu,)
if num2>=21:
    print("Limit reached. You fail")
else:
    print("Good Job, code cracked in",num2, "tries")    


#startcondition
#i=1
#r=1
###while(test condition)
#while i<=10000:
##block of code to execute
    #print(chr(r),end="")
    #r=r+1

