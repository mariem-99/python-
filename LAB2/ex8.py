def nb_words(s):
   i=0
   while i<len(s) :
    words=s.split()
    return (len(words))

s=input("enter a sentence:")
print(f"the number of words in the sentence is {nb_words(s)}")


