import random
def guess():
    x=random.randint(1,100)#random number 
    print("guess the number between 1 and 100 ")
    y=int(input("enter your guess :"))
    while(y!=x):#if the guess is right the loop will stop and you win 
        if(y<x):
            print("too low!")
        else:
            print("too high!")
        y=int(input("try again :"))
    print("congratulation ! you win !!! XD")

#main
#everithing is in the function guess 
#so we just call it 
guess()
