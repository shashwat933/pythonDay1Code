from functools import reduce

class Employee:

    def __init__(self,id,name,salary,city):
        self._id=id
        self._name=name
        self._salary=salary
        self._city=city

    def get_salary(self):
        return self._salary
    
    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name=name

    def set_salary(self, salary):
        self._salary = salary

    def set_city(self, city):
        self._city = city

    def __str__(self):
        return f"Employee Id: {self._id}, Name: {self._name}, Salary: {self._salary}, City: {self._city}"


class Manager(Employee):

    def __init__(self, id, name, salary, city, department):
        super().__init__(id, name, salary, city)
        self._department = department

class Management:

    def __init__(self):
        self.employees=[]

    def add_emp(self,emp):
        
        self.employees.append(emp)
    
    def show_emp(self):
       for i in self.employees:
           print(f"Employee Id:{i._id} Name:{i._name} Salary:{i._salary} City:{i._city}")

    def search_by_name(self):
        name=input("Enter the name of the employee : ")
        f=0
        for i in self.employees:
            if(i._name==name):
                print(f"Employee with name:{name} is present")
                print("")
                f=1
                return
        if(f==0):
            print(f"Employee with name:{name} is not present")
            print("")

    def search_by_city(self):
        print("Enter the city of the employee")

        city=input()
        f=0
        for i in self.employees:
            if(i._city==city):
                print(f"Employee with city name:{city} is present")
                print("")
                f=1
                return
        if(f==0):
            print(f"Employee with city name:{city} is not present")
            print("")
        
    
    def edit_employee(self):
        print("Please enter the id of the employee")
        emp_id=(int)(input())
        idx=-1
        for index, i in enumerate(self.employees):
            if(i._id == emp_id):

                idx=index
                break
        if(idx==-1):
            print("No employee found")
            print("")
            return
        print("If you want to change name of the employee , enter YES")
        response=input()
        if(response=='YES'):
            print("Enter name")
            name=input()
            (self.employees[idx]).set_name(name)
        print("If you want to change city of the employee , enter YES")
        response=input()
        if(response=='YES'):
            print("Enter city")
            name=input()
            (self.employees[idx]).set_city(name)
        print("If you want to change salary of the employee , enter YES")
        response=input()
        if(response=='YES'):
            print("Enter salary")
            salary=(float)(input())
            self.employees[idx].set_salary(salary)

    def delete_by_id(self):
        print("Enter the id")
        emp_id=(int)(input())
        for index,value in enumerate(self.employees):
            if(value._id==emp_id):
                del self.employees[index]
                return
            
        print("Employee not found")
        print("")

    
    def delete_by_name(self):
        print("Enter the name")
        name=(input())
        for index,value in enumerate(self.employees):
            if(value._name==name):
                del self.employees[index]
                return   
        print("Employee not found") 
        print("")

    def view_name_in_capital(self):
        emp_name_list=list(map(lambda emp:emp.get_name().upper() , self.employees))
        print(emp_name_list)

    def filter_emp_salary(self):
        salary=(int)(input("Enter salary"))
        emp_list=list(filter (lambda emp:emp.get_salary() > salary,self.employees))
        for i in emp_list:
           print(f"Employee Id:{i._id} Name:{i._name} Salary:{i._salary} City:{i._city}")
        

    def cal_total_salary(self):
        total = reduce(lambda a, b: a+ b.get_salary(), self.employees,0)
        print(total)


class Manager(Employee):
    def __init__(self, id, name, salary, city, department):
        super().__init__(id, name, salary, city)
        self._department = department

    def __str__(self):
        return f"{super().__str__()}, Department: {self._department}"

def add_new(manage):
    print("Enter employee id")
    id=(int)(input())
    print("Enter employee name")
    name=input()
    print("Enter employee salary")
    salary=(float)(input())
    print("Enter employee city")
    city=input()
    print(id,name,salary,city)
    emp=Employee(id,name,salary,city)
   
    manage.add_emp(emp)

    print("Employee Added")
    print("")

def view_emp(manage):
    manage.show_emp()
    print("")


def search_emp(manage):
    print("1:Search By Name")
    print("2:Search By City")    
    choice=(int)(input())
    if(choice==1):
        manage.search_by_name()
    else:
        manage.search_by_city()


    

def edit_emp(manage):
    manage.edit_employee()


def delete_emp(manage):
    print("1:Delete employee on the basis of employee id.")
    print("2:Delete employee on the basis of name.")
    choice=(int)(input())
    if(choice==1):
        manage.delete_by_id()

    else:
        manage.delete_by_name()

def view_name(manage):
    manage.view_name_in_capital()

def  filter_salary(manage):
    manage.filter_emp_salary()

def total_salary(manage):
    manage.cal_total_salary()

def start():
    manage=Management()
    while(1):
    
        print("Select the options and press enter->")
        print("1:Add a new employee to the list.")
        print("2:View all employees.")
        print("3:Search for employees.")
        print("4:Edit employee detials.")
        print("5:Delete an employee.")
        print("6.Show all the names of employee.")
        print("7.Filter salary")
        print("8.Show total salary expenditure")
        print("9:Exit.")
        num=(int)(input())
        if(num<1 or num>9):
            print("Enter correct choice")
        elif(num==1):
            add_new(manage)
        elif(num==2):
            view_emp(manage)
        elif(num==3):
            search_emp(manage)
        elif(num==4):
            edit_emp(manage)
        elif(num==5):
            delete_emp(manage)
        elif(num==6):
            view_name(manage)
        elif(num==7):
            filter_salary(manage)
        elif(num==8):
            total_salary(manage)
        else:
            break



start()



    
