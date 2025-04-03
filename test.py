import datetime

#creating a specific date
#datetime.time(year,month,day)
date=datetime.date(2023,3,12)#output example 2023-03-12

#getting Today's date
#This gets the current date based on your system’s clock.
today= datetime.date.today() #today() is a method
#example output (2025-04-03)

#creating a specifiv time 
#datetime.time(hour, minute, second)
time=datetime.time(12, 30, 9) #output: 12:30:09

#Getting the Current Date & Time
#This captures the exact current date and time when the code runs.
now = datetime.datetime.now()#output : 2025-04-03 12:12:45.923624

# Formatting the Date & Time
now = now.strftime("%H:%M:%S %m-%d-%Y")
'''
.strftime() converts the date/time object into a formatted string.

The format used:

%H → Hours (24-hour format)

%M → Minutes

%S → Seconds

%m → Month (as a number)

%d → Day

%Y → Year (4-digit format)
'''




 

