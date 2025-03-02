def gcd(a,b):
    while a!=b:
        if a<b:
            b-=a
        else:
            a-=b
    return a
a=int(input("enter a: "))
b=int(input("enter b: "))
s=gcd(a,b)
print(f"GCD of {a} and {b} is {s}")