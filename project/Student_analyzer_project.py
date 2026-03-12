print("     ********** :- welcome in Student Analyzer portal-:***************")
names=[]
marks=[]
print("\n")

n=int(input("Enter the total no of student:- "))
for i in range (n):
    name=input(f"Enter the student name {i+1}:-")
    mark=int(input(f"Enter the mark of {name}:-"))
    names.append(name)
    marks.append(mark)
print("\n :- Result of student -:")
for i in range(n):
    print(f"{names[i]} scored {marks[i]} marks")
average=sum(marks)/len("marks")
print("average of the total mark:-",average)
print("heighest mark of the student:-",max(marks))
print("lowest mark of the student:-",min(marks))
print("          :- Result of the Student  -:      ")
for i in range(n) :
          m=marks[i]
          if(m>=85):
               Grade="A"
          elif(m>=70):
                 Grade="B"
          elif(m>=55):
                 Grade="C"
          elif(m>=40):
                 Grade="D"
          else:
                 print("Fail")
          if (m>=40):
                 status="passed"
          else:
                 status="Failed"
          print(f"{names[i]} => {status}, Grade: {Grade}")

          
print(" thanku for visit me ")
