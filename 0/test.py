'''
item="apple"
item2="banana"
price1=1.5
price2="0.75"
quantity1=3
quantity2="5"

total_cost=(price1 * quantity1) + float(price2) * int(quantity2) #price2 is str i turned it to float and the same for quantity2 to int 

print("the total cost is:", total_cost)#there is "," missing 
'''
'''
num1=float(input("enter number 1: "))
num2=float (input("enter number 2: "))
sum=num1+num2
print("sum=",sum)
product=num1*num2
print(f"product=",{product})
'''
age=int(input("enter your age= "))

answer=input("do you have an ID? yes or no")
if  ((age>=18 )and(answer.lower()=="yes")):
    print("you are eligible to vote!")
else:
    print("ypu are not eligible to vote!")
