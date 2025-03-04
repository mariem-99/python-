def substring(s1 ,s2):
    if s2 in s1 :
        return True 
    return False 

#main
s1=input("enter the first string :")
s2=input("enter the second string :")
if (substring(s1,s2)):
    print(f"{s2} is a substring of {s1}")
else:
    print(f"{s2} is not a substring of {s1}")
