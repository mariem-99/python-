import numpy as np 
def get_student():
    n=int(input("Enter the number of students: "))
    students =[] #create an empty list 
    for i in range(n):
        #append the list with the input
        name= input(f"Enter the name of the student {i+1}:") 
        students.append(name)
    return students



def get_course():
    m=int(input("enter the number of courses:"))
    courses =[] #create an empty list              
    for i in range(m):
        #append the list with the input
        name=input(f"Enter the name of the course {i+1}:") 
        courses.append(name)
    return courses 




def get_marks(students,courses):
    grades={} #create an empty dictionary 
    for student in students:#loop through the students list 
        grades[student]={}#cerate a nested dictionary 
        for course in courses:#loop through the courses list 
            midterm = int(input(f"enter {student}'s midterm mark for {course}:"))
            final=int(input(f"enter {student}'s finam exam mark for {course}:"))
            
            #store the marks in the nested dictionary 
            grades[student][course]={"midterm": midterm,"final": final}
    return grades #return the final directory 




def final_grade(grades):
    results={}#create an empty dictionary to store the final grades 
    print("📊final grades :")
    for student in grades:
        print(student)#print the student name
        results[student]={}#store each student's grades in a nested directory  
        for course in grades[student]:#loop through the nested directory 
            midterm=grades[student][course]["midterm"]#get the midterm mark 
            final=grades[student][course]["final"]#get the finam mark 
            total=(midterm * 0.3)+(final * 0.7)#calculate the total mark
            print(f"{course} : {total:.2f}")
            results[student][course]=total #store the total mark in the nested directory 
    return results #return the computed grades 
            
            
def best_student (results):
    best_avg=-1 #initialize the best average to a very low number 
    best_student=""#initialize the best student to an empty string 
    for student in results:#loop through the results directory 
        avg=sum(results[student].values()) / len(results[student]) #calculate the avg of each student
        if avg > best_avg:#check if the student average is higher than the best average  
            best_student=student #store the student name
            best_avg=avg #store the student's avg 
            
    print(f"🏆the best student is {best_student} with an average of {best_avg:.2f}")#print the best student and the average 
    
    

def worst_student(results):
    worst_avg=101 #initialize the worst average to a very high number 
    worst_student=""#initialize the worst student to an empty string 
    for student in results :#loop through the results directory 
        avg= sum(results[student].values()) / len(results[student])#calculate the avg of each student
        if avg <worst_avg:#check if the student average is lower than the worst average or not 
            worst_student=student#store the student name
            worst_avg=avg #store the student's average 
            
    print(f"📉the worst student is {worst_student} with an average of {worst_avg:.2f}")#print the worst student and the average
    
    

def class_avg(results):
    total=0 #initialize the total to 0
    count=0 #total number of couurses
    for student in results:#loop through the results directory 
        for course in results[student]:#loop through the nested directory
            total+=results[student][course]#add the total of each student to the total  
            count+=1 #count the number of courses
    avg= total/count #compute the average 
    return avg #return the average 


def course_wise_averages(courses,results): 
    course_average={} #create an empty dictionary to store the average of each course 
    for course in courses: #loop through the courses list
        total=0 #initialize the total to 0
        count=0 #number of students who took the course
        for student in results: #loop through the grades directory
            if course in results[student]:
                total+=grades[student][course]["midterm"] * 0.3 + grades[student][course]["final"] * 0.7 #calculate total grade for the course 
                count+=1 #increment the count   
        if count > 0:#check if the count is greater than 0
            course_average[course]=total/count #compute the average of the course 
    print("\n📊course averages:")
    for course, avg in course_average.items():
        print(f"{course} : {avg:.2f}")
    
    easiest_course=max(course_average,key=lambda x: course_average[x]) #get the easiest course 
    hardest_course=min(course_average,key=lambda x: course_average[x]) #get the hardest course 
    print(f"\n✅the easiest course is {easiest_course} with an average of {course_average[easiest_course]:.2f}")
    print(f"❌the hardest course is {hardest_course} with an average of {course_average[hardest_course]:.2f}")
    return course_average #return the course averages 



def top_3_students(results):
    top_3=[] #create an empty list to store the top 3 students 
    for student in results:#loop through the results directory 
        avg=sum(results[student].values()) / len(results[student])#calculate the avg of each student
        top_3.append((student,avg))#append the list with the student name and the average 
    top_3.sort(key=lambda x:x[1],reverse=True)#sort the list in descending order 
    print("\n🏆top 3 students:")
    for i in range(3):#loop through the top 3 students 
        print(f"{i+1}. {top_3[i][0]} : {top_3[i][1]:.2f}")#print the student name and the average
        
        
        
def search(students,grades):
    name=input("enter the name of the student to see their grades :") # get the name of the student 
    if name in students: #check if the name is in the students list 
        print(f"{name}'s grades:")
        for course in grades[name]:
            midterm=grades[name][course]["midterm"] #get the midterm mark
            final=grades[name][course]["final"] #get the final mark 
            print(f"{course} : midterm = {midterm}, final={final}")
            
#main

#call the functions
#list of students   and courses  
students=get_student()
courses=get_course()
#dictionary of grades
grades=get_marks(students,courses)    

#calculate the final grades based on the marks 
results=final_grade(grades)    
    
#display the best and the worst students   
best_student(results)
worst_student(results)    
        
#display the class average
class_average=class_avg(results)    
print(f"\n📊class average : {class_average:.2f}")    

#display the course wise averages 
course_wise_averages(courses,results)    
     
#display the top 3 students 
top_3_students(results)    

#search for a student's grades 
search(students,grades)     
            
        
            