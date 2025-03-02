ch=input("enter a string: ")
ch1="" #empty 

for i in range(len(ch)-1,-1,-1):#starting from the last character
    ch1+=ch[i] #each c will be added to the ch1 

print(f"the string {ch} in reserve order is {ch1}")
#simpler method
'''
ch = input("Enter a string: ")
ch1 = ch[::-1]  # Reverse the string using slicing

print(f"The string {ch} in reverse order is {ch1}")
'''