while(True):
    t=input("Enter choice\n1. Start\n2. End\n")
    if(t=="Start" or t=="start"):
        n= int(input())
        if n>0:
            print("The number is positive")
        elif n==0:
            print("The number is zero")
        else:
            print("The number is negative")
    else:
        break
