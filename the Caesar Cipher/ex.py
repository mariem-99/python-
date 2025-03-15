#encrypt the message 
def encrypt(ch,n):
    ch1=""
    i=0
    while i<len(ch):
        if ((ch[i]=="Z") or (ch[i]=="z")):
            ch1+=chr((ord(ch[i]))-(26 - n ) )
        elif ch[i].isalpha():
            ch1+=chr((ord(ch[i]))+n)
        else:
            ch1+=ch[i]
        i+=1    
    return ch1

#decrypt the message 
def decrypt(ch,n):
    ch1=""
    i=0
    while i<len(ch):
        if ch[i].isalpha():
            if ch[i] == 'A' or ch[i] == 'a':
                ch1 += chr(ord(ch[i]) - (26 - n))
            else:
                ch1 += chr(ord(ch[i]) - n)
        else:
            ch1 += ch[i]
        i += 1
    return ch1


#MAIN 
n=int(input("enter the shift number :"))
ch=input("enter the message:")
encrypted = encrypt(ch, n)
decrypted = decrypt(encrypted, n)

print(f"The encrypted message is: {encrypted}")
print(f"The decrypted message is: {decrypted}")