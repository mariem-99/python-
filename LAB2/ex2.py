def palindrome(ch):
    for i in range(len(ch)//2):
        if (ch[i]!=ch[len(ch)-i-1]):
            return False
    return True  
    
ch=input("enter a string= ")
if (palindrome(ch)==True ):
    print(f"{ch} is palindrome")
else:
    print(f"{ch} is not palindrome")

