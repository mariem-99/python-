def pangram(s):
    s=s.lower()
    alpha_set=set()#create an empty set 
    for c in s:#loop through the string 
        if c.isalpha():#check if the character is an alphabet 
            alpha_set.add(c)#add the character to the set 
    return len(alpha_set)==26#check if the length of the set is 26


#main    
s=input("enter a sentence:")
if (pangram(s)):
    print(f"{s} is pangram")
else:
    print(f"{s} isn't pangram")