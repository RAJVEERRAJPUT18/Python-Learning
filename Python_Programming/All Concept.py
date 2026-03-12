                              # if-else statement
# Check no even or odd
# a=input("Enter the frist no=")

# if (int(a)%2):
#     print('this is odd no ')
# else :
#     print("this is even no")

# check the lagest num of given num.

# print("Enter the num and check the lagrgest num ")
# a =float(input("enter the frist no=" ))
# b= float(input("enter the second num ="))
# c =float(input("enter the third no=" ))
# d =float(input("enter the fourth num ="))
# if (a>=b and a>=c and a>=d):
#     print("a is the largest num")
# elif(b>=a and b>=c and b>=d):
#     print("b is largest")
# elif(c>a and c>=b and c>=d):
#     print("c is largest ")
# elif(d>=a and d>=b and d>=c):
#     print("d is largest")


# Electricty Bill Calculater unit
# print(":-welcome:-")
# Value=float(input("Howmany use the electricty  in unit:= "))

# match Value:
#     case Value if(Value<=0):
#         print("your Electricty bill amount is Rs-0.00 ")

#     case Value if (Value>0 and Value<=100) :
#         print("your Electricty bill amount is Rs-",Value*5)
#     case Value if (Value>100 and Value<=200):
#         print("your Electricty bill amount is Rs-",Value*7)

#     case Value if (Value>200 and Value<=300):
#         print("your Electricty bill amount is Rs-",Value*10)
#     case Value if (Value>300 and Value<=1000):
#         print("your Electricty bill amount is Rs-",Value*
                                                             # fibonacci series

# def fib(n):
#     if n <= 1:
#         return n
#     else :
#         return fib(n-1)+fib(n-2)
    
# n=int(input("enter the num whiches you want to term of print:-"))

# print("fibonacci sequense")
# for i in range(n):
#     print(fib(i))

# a=[2,3,4,4,7,8,90,57,9598]
# print(a)
# a.append(20)
# print(a.index(57))



# m=a.copy()
# print(m)

# a.extend(
                                                               #  list
# lst=[i*i for i in range (10) if i%2==0]
# print(lst)
# raaz=(3,4315,546,876,867,8,4)
# print(type(raaz),raaz)
# import this

# s1={3,5,6,46,4,4,7,75,5,4,5,}
# s2={2,1,4,5,8,7,4,5,2,1}
# m=s1.union(s2)
# print(m)
# n=s1.intersection(s2)
# print(n)
# p=s1.difference(s2)
# print(p)
# q=s1.issuperset(s2)
# print(q)
                                                           # dicionary
# info = {'name':'Karan', 'age':19, 'eligible':True}
# # print(info)
# # print(info.keys())
# # print(info.values())

# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 
  
# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}

# # ep1.update(ep2)
# # ep1.clear()
# # ep1.pop(122)
# try :
#    ep1. popitem()
#    del ep1[122]
#    print(ep1) 
# except:
#    print(NameError)
# print(ep2)
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

#try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
#except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")
 

  



                                                  # /Error handling 
                                                       # exception Handling
# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
  

# except Exception as e:
  
  
# finally :

#    n=int(input("enter the num"))

#    # def factorial(n) :
#    if(n==0 or n==1):
#       print( "Radhey Radhey")
#    else :
#       print("Ram Ram ")
 

# try:
#     x = 5 / 1
#     print("No error.")
# finally:
#     print("Cleanup complete.")
# 
# 
# rint("This still runs before the crash.")

# short hand if else

# a= 334

# b=78
# print("a") if(a>b) else print("=") if(a==b) else print("b")
     
      
                                                 #enumerate function in python

# items=[ "mango","papaya","banana","apple"]

# for index, item in enumerate(items,start=1):
         
         
#          print(f"{index} .{item}")
#          if (index== 3):
#             print("this is my favrauit fruit
# from math import sqrt,pi,pow

# print(pow(7,3))

# import math as m
# a=m.pow(2,3)
# print(a)
 
