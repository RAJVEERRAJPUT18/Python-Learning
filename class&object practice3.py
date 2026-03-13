# #      1. Create a BankAccount class with attributes account_number, owner_name,and balance.,Add methods to deposit ,withdraw, and check balance
# class BankAccount:
#     def __init__(self,Account_number,owner_name,__balance):
#           self.Account_number=Account_number
#           self.owner_name=owner_name
#           self.__balance=__balance
        

#     def set_deposit(self,deposit_ammount,__balance):
#          self.deposit_amount=deposit_ammount
#          self.new__balance=(__balance+deposit_ammount)
#          print(f"Deposited Amount-{self.deposit_amount},Total balance is-{self.new__balance}")
     
#     def set_withdrawl(self,withdrawl_ammount,__balance):
#          self.withdrawl_amount=withdrawl_ammount
#          self.new__balance=(__balance-withdrawl_ammount)
#          print(f"withdrawl Amount-{self.withdrawl_amount},Total balance is-{self.new__balance}")

#     def check_balance(self):
#          print(f"Balance is-{self.new__balance}")

# u1=BankAccount(123,"Raaz",10_000)
# u2=BankAccount("Ramu",456,20_0000)
# print(u1.owner_name,u1.Account_number)
# print(u1.set_deposit(2000, 10_000))
# print(u1.set_withdrawl(2000, 10_000))
# # print(u1.check_balance())

### 2. Create a class book of follwing atributes


# class Book:
#     reviewcount=0

#     def __init__(self,title,auther):
#         self.title=title
#         self.auther=auther
          

        
#     def add_review(self,add_review):
#         

#     # @classmethod
#     # def get_count_review(cls):
#     #     cls.add_review.reviewcount=add_review.reviewcount
#     #     print(f"total review-{cls.add_review.reviewcount")

# Bookno1=Book("Poor Dad & Rich Dad","Rajsahmani")
# print(Bookno1.auther, Bookno1.title)
# print(Bookno1.add_review("This is a best book for student"))
# print(Bookno1.get_count_review())


##############  3.Create a class Student  with private  attributes _name, _roll_no, and _marks.
# Provide getter and setter methods with validation (e.g., marks cannot be 
# negative, roll number has to be between 1 & 100 & name cannot be empty).

# class student:
#     def __init__(self,__name):
#         self.__name=__name
        
#     def set_info(self,__rollno,__marks):
#         if(__rollno>0 and __marks>0 and __marks<100):
#             self.__rollno=__rollno
#             self.__marks=__marks
#         else:
#             print("please Enter valid roll no or marks")

#     def get_info(self):
#         print(f"Student name is {self.__name},Student Rollno is-{self.__rollno},Student merks-{self.__marks}")
    

# Stu1=student("Raaz")
# print(Stu1.set_info(25,10))

# print(Stu1.get_info())


##############  4.Create a class shape with a method area().
# Create subclasses circle,rectangle , tringale and  that  the area() 
# method.

# class shape:
#     def get_area(self):
#         print("Area is =shape")

# class circle(shape):
#     def get_area(self):
#         print("Area is =circle")

# class rectangle(shape):
#     def get_area(self):
#         print("Area is =rectangle")

# class tringle(shape):
#     def get_area(self):
#         print("Area is =tringle")

# a1=circle()
# a2=rectangle()
# print(a2.get_area())

############### 5. 
# . Create a base class  with vehicle attributes like brand brand and modal model.
# Create two sbuclasses car and bike  that add extra attributes - seats (in Car) & 
# engine_cc (in Bike).

# class vehicle:
#     print("Welcome in my soroom")
#     def __init__(self,brand,modal):
#              self.brand=brand
#              self.modal=modal
    
# class car(vehicle):
#        def __init__(self, brand, modal,seats):
#             super().__init__(brand, modal)
#             self.seats=seats
#             print(f"Car brand is-{self.brand},Car modal is -{self.modal},total seats in car is-{self.seats} ")

# class bike(vehicle):
#       def __init__(self, brand, modal,engine_cc):
#             super().__init__(brand, modal)
#             self.engine_cc=engine_cc
#             print(f"Bike brand is-{self.brand},Bike modal is -{self.modal},Capecity of engine-{self.engine_cc} ")
            

# v1=car("TATA","CURV",4)     
# v2=bike("TVS","APACHE RTR","160CC")




############### 
# 6.Create an  abstract class Employee with an abstract method and calculate_salary().Create subclasses Intern,FullTimeEmployee , and contractempolee implement the method differently. 

# from abc import ABC ,abstractmethod

# class employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class intern(employee):
#     def calculate_salary(self):
#         print(10_000)
    
# class FulltimeEmolyee(employee):
#     def calculate_salary(self):
#         print(30_000)

# class contractEmployee(employee):
#     def calculate_salary(self):
#         print(50_000)

# emp1=intern()
# emp1.calculate_salary()
# emp2=contractEmployee()
# emp2.calculate_salary()



############ 7.

# class player:
#     player_count=0
#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#         player.player_count+=1

#     def get_info(self):
#         print(f"Player name is-{self.name},Player level is-{self.level}")
#     @classmethod
#     def get_player_count(cls):
#         print(f"Total player is-{cls.player_count}")


# p1=player("Raaz","1st")
# p4=player("dhani","4st")
# p3=player("vikas","3st")
# p2=player("chhavi","2st")
# p2.get_info()
# player.get_player_count()



