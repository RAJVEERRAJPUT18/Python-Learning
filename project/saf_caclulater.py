print("Welcome !")
try :
   a=int(input("Enter the frist num:-"))
   b=int(input("Enter the second num:-"))
   sum=(a+b)
   sub=(a-b)
   multi=(a*b)
   divi=(a/b)
   print("sum of the num is :-",sum)
   print("sub of the num is :-",sub)
   print("multi of the num is :-",multi)
   print("divi of the num is :-",divi)
except ValueError:
   print("Enter value is not integer")
except ZeroDivisionError :
   print("You can not divigion by zero")

finally :
   print("Complete the operations")  
