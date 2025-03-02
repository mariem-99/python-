def calculate_av(total,nb):
    return total/nb

nb=int(input("how many number do you have ? ="))
total=0
for i in range(nb):
    a=int(input("enter your number "))
    total+=a

print(f"the average of your numbers is {calculate_av(total,nb)}")