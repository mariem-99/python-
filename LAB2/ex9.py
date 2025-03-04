def prime(a):
    nb=0
    for i in range(1,a+1):
        if a%i==0:
            nb+=1
    return nb==2      

    
a=int(input("enter a="))
if (prime(a)):
    print(f"{a} is prime")
else:
    print(f"{a} isn't prime")
