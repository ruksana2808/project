

class Employee(object):

     def __init__(self,name,salary):
        self.name= name
        self.salary=salary

     def details(self):
        #print('My name is  {}\t'.format(self.name))
        print("and his salary is {} per month".format(self.salary))

class alex(Employee):

    def details(self):
        print("The salary of {} is {} per month".format(self.name,self.salary)) #polymorphishm
        

class alen(Employee):  #inheritance
    def __init__(self, name, salary, company):
        self.company = company

        Employee.__init__(self,name,salary)

    def identify(self):
        print("{} is the employee in {}".format(self.name,self.company))


#obj instant

a=alen("Alen",20000,"XYZ")
a.identify()
a.details()

b=alex("Alex",15000)
b.details()