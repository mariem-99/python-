def delete_vowels(s):
    vowels='aeiuoAEIUO'
    for i in vowels:
        s=s.replace(i,'')
    return s

#main
s=input("enter a sentence ")
print(f"the sentence without vowels is {delete_vowels(s)}")