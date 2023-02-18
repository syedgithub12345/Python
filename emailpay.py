'''
Question- 
Create a class employee with following properties
-First Name
-Last Name
-Pay
-Email : should be automatically generated as
    Firstname+','+Lastname+"@company.com"
''' 

class Employee():
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay

    def mail(self):
        self.m=str(self.fname)+str(self.lname)+"@company.com"
        return self.m


a = input("First name is :")
b = input("Last name is :")
p = eval(input("Pay is :"))

det=Employee(a,b,p)

print(det.mail())
print(p)