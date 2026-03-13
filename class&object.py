# class physithorpy:
#     name="Raaz"
#     subject="python"
#     cgpa="8.2"
# stu1=physithorpy()
# stu2=physithorpy()
# print(stu1.name)
# print(stu2.name)



# class student:
#     def __init__(self,name,cgpa,sub):
#         self.name=name
#         self.cgpa=cgpa
#         self.sub=sub
#     def getcgpa(self):
#         return self.cgpa

# stu1=student("Raaz",8.7,"python")
# stu2=student("Ram",6.7,"python")
# stu3=student("mohit",5.7,"python")
# print(f"{stu2.name} has cgpa={stu2.getcgpa()}")
# print(stu1.cgpa)
# print(stu3.cgpa)


# methods of the class

# Instance method
# class laptop:
#     brand_name="Dell"
#     color_name="Brown"

#     def __init__(self,RAM,STORAGE):
#         self.RAM=RAM
#         self.STORAGE=STORAGE
#     def get_info(self):# instance method 
#         print(f"Laptop name-{self.brand_name},laptop color-{self.color_name},laptop ram-{self.RAM},laptop storage-{self.STORAGE}")

#     @classmethod# class decorater
#     def get_brand(cls):#class method
#         print(f"laptop brand-{cls.brand_name}")


# #####static method
#     @staticmethod
#     def calc_price(prise,discount):
#         final_prise=prise-(discount*prise/100)
#         print(f"discounted prise={final_prise}")
        
# L1=laptop("8GB","512SSD")
# L2=laptop("4GB","256SSD")
# L1.get_info()
# L2.get_brand()
# L1.calc_price(40_000,20)\



# create a  online product store (name,prise)
# terack total product being created.
# create a static method to calculate discount on each product based on a %parameter

# class product:
#     shop_name="Rajput electonics store"
#     count=0
#     def __init__(self,name,prise):
#         self.name=name
#         self.prise=prise
#         product.count+=1

#     def get_info(self):
#           print(f"shop name={self.shop_name},Product name={self.name},Product prise Rs-{self.prise}")

#     @classmethod
#     def get_count(cls):
#          print(f"Total product in store={cls.count}")
#     @staticmethod
#     def cal_discount(prise,discount):
#          discounted_prise=prise-(discount*prise/100)
#          print(f"discounted prise={discounted_prise}")
# p1=product("mobile",15000)
# p2=product("charger",2000)
# p1.get_info()
# p1.cal_discount(p1.prise,15)
# product.get_count()

#########################Incapsulation
# data hiding

# class bankaccount:
#     def __init__(self,name,balance):
#         self.name=name             #public
#         self.__balance=balance #privete
        
#     def get_info(self):    #getter function
#         print(f"balance rs={self.__balance}")
#     def set_balance(self,newbalance):      #setter function
#         self.__balance=newbalance
#         print(f"balance is rs-{self.__balance}")
# acc1=bankaccount("raaz",10000)
# # print(acc1.name,acc1.get_info()) 
# print(acc1.set_balance(20000))                   #private ko direct class ke bahr access nhi ke skte h



####################################inheritance
########## singal level inheritance
# class employe:
#     start_time="10am"
#     end_time="8pm"
#     count=0
#     def change_time(self,new_start_time):
#         self.start_time=new_start_time
#     @classmethod
#     def get_count(cls,role):
#         cls.role=role
#         print(f"{cls.role}-{cls.count}")

# class teacher(employe):
#     def __init__(self,name,sub):
#         self.name=name
#         self.sub=sub
#         teacher.count+=1
#         print(f"Teacher name-{self.name},subject name-{self.sub},college start time-{self.start_time},college closed time-{self.end_time}")

# class Admin(employe):
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#         # Admin.count+=1
#         print(f"Admin name-{self.name},Admin role-{self.role},college start time-{self.start_time},college closed time-{self.end_time}")

# emp1=teacher("Raaz","Physics")
# emp2=teacher("sukhdev","mathe")
# emp3=teacher("dilasaram","english")
# emp4=teacher("jitendra","Physics")
# emp5=Admin("Sudhir tripathi","manager")
# emp6=Admin("Saumya","principal")
# emp7=Admin("kushvah ji","cashear")

# # emp1.change_time("8am")

# emp1.get_count("teacher")
# emp2.get_count("Admin")


###### multi level inheritance

# class employe:
#     start_time="10am"
#     end_time="8pm"
#     count=0
   
# class Admin(employe):
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#         print(f"Admin name-{self.name},Admin role-{self.role},college start time-{self.start_time},college closed time-{self.end_time}")

# class Accountant(Admin):
#     def __init__(self, name, role,salary):
#         super().__init__(name, role)
#         self.salary=salary

# emp1=Accountant("Raaz","CA",25000)
# print(emp1.name,emp1.role,emp1.salary)



##################### multilevel inheritance

# class teacher:
#     def __init__(self,salary):
#         self.salary=salary
        
# class student:
#     def __init__(self,cgpa):
#         self.cgpa=cgpa

# class TA(teacher,student):
#     def __init__(self, salary, cgpa,name):
#         super().__init__(self,salary)
#         student.__init__(cgpa)
#         self.name=name
# t1=TA(20000,9.8,"monu")
# print(t1.name,t1.salary,t1.cgpa)




################## Abstractact classes

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class lion(Animal):
#     def make_sound(self):
#         print("Rore!")
# class cat(Animal):
#     def make_sound(self):
#         print("Meaw")

# lion=lion()
# lion.make_sound()

# cat=cat()
# cat.make_sound()


###############polymorphism
#######################overriding method
# class employee:
#     def get_designation(self):
#         print("designation=employee")
# class teacher(employee):
#      def get_designation(self):
#         print("designatioj=teacher") # overriding method of polymorphism 

# t1=teacher()
# t1.get_designation()

############duck typeing method

# class accountant:
#     def get_designation(self):
#         print("designation=accountant")
# class teacher():
#      def get_designation(self):
#         print("designatioj=teacher") 

# t1=teacher()
# t1.get_designation()

# acc1=accountant()
# acc1.get_designation()