def find_fac(a):
    if (a==0 or a==1):
        return 1
    else:
        return a*find_fac(a-1)

a=int(input("enter a="))    
print(f"the factorial of {a} is {find_fac(a)}")