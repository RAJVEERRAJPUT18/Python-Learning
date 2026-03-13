# Salary
# Write a program that takes  as input. Using conditional statements, 
# calculate the  
# final tax rate
# based on these rules:
# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%
# salary=int(input("Enter the salry amount :-"))
# if(salary<=30000):
#     tax=salary*5/100
#     print("Total taxamount of the salary:-",tax)
# elif(30000<=salary or salary<=70000):
#     tax=(salary*15/100)
#     print("Total taxamount of the salary:-",tax)
# elif(salary>=70000):
#     tax=(salary*25/100)
#     print("Total taxamount of the salary:-",tax)
# else:
#    print("'Warning' Enter the valod input")

# Q2.
# Write a function that takes two integers a and b prints all even 
# numbers between them (inclusive).

# def even_num(a,b):
#     for i in range(a,b):
#         if(i%2==0):
#            print("even no is:-",i)
#         i+=1
# a=int(input("Enter the frist num:- "))
# b=int(input("Enter the second num:- "))
# print(even_num(a,b))




# num=int(input("Enter the num:-"))
# def Digit(num):
#     for i in str(num):
#         print(i)
# Digit(num)


# num=int(input("Enter the num:-"))
# def Digit(num):
#     count=0
#     for i in str(num):
#         print(i)
#         count+=1
#     print("total count of the num",count)
    
# Digit(num)

# reverse the num

# n=int(input("Enter the num:-"))

# def reversnum(n):
    
#     while n>0:
#         digit=n%10
#         n//=10
#     print(digit)
# print(reversnum)


# num=int(input("Enter the num:-"))
# def Digit(num):
#     count=0
#     i=0
#     while num>0:
#         digits=num%10
#         num//=10
#         count+=1
#         i=i+digits
#         print(digits)
#     print("total count of the num",count)
#     print("Sum of all digit:-",i)

# Digit(num)


#  Write a program to print all numbers from 1 to 100 that are divisible by both 3 
# and 5.

# for i in range(1,100):
#        if i%3==0 and i%5==0:  
#               print("Total num disible by both",i)
#        else:
#               continue

# Design a program to continuously input a number  from user & print if it is 
# positive or negative until the user enters “Quit”
# print("Enter only integer num if you want the quick then you pres any button notinclude integer num")
# while True:
#     n=(input("Enter the num:-"))
#     if n=='quick':
#         break


# Check the prime num 

# n=int(input("Enter the num:=-"))
# for i in range(2,n-1):

#   if n%i==0:
#     print("This is not  prime num")

#   else :
#     print("this is  prime num")
#   break

# number gessing game 
# n=int(input("Enter the num bitbeen 1 to 100 : "))
# for i in range(1,100):
#     num=int(input("Gess the num: "))
#     if num==n:
#       print("Carrect num")
#       break
#     elif num>n:
#        print("To heigh ")
#     elif num<n:
#        print("to low")

    
#############################Assignment 2 complete

  