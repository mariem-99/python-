def fahrenheit(c):
    f=(c * (9//5))+ 32 
    return f

c=float(input("enter the temperature "))
f=fahrenheit(c)
print(f"the fahrenheit temperature is {f}")
