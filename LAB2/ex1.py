def larger_number(ar1,ar2):
    if(ar1>ar2):
        return ar1
    else:
        return ar2
 
ar1=int(input("enter the first argument"))
ar2=int(input("enter the second argument"))
print(f"the larger number is {larger_number(ar1,ar2)}")
