from functools import reduce

def add_new(emp):
    print("Enter employee id")
    emp_id=input()
    print("Enter employee name")
    name=input()
    print("Enter employee salary")
    salary=(float)(input())
    print("Enter employee city")
    city=input()
    emp.append({"employee_id":emp_id,"name":name,"salary":salary,"city":city})

    print("Employee Added")
    print("")

def view_emp(emp):
    for i in emp:
        print(f"Employee id:{i["employee_id"]} name:{i['name']} salary:{i['salary']} city:{i['city']}")
        print("")
    print("")

def view_name(emp):
    emp_name_list=list(map(lambda emp:emp['name'].upper() , emp))
    print(emp_name_list)


def filter_salary(emp):
    salary=(int)(input("Enter salary"))
    emp_list=list(filter (lambda emp:emp['salary'] > salary,emp))
    print(emp_list)
    


def total_salary(emp):
    total = reduce(lambda a, b: a+ b['salary'] , emp,0)
    print(total)

def search_emp(emp):
    print("1:Search By Name")
    print("2:Search By City")    
    choice=(int)(input())
    if(choice==1):
        search_emp_by_name(emp)
    else:
        search_emp_by_city(emp)

def search_emp_by_name(emp):
    print("Enter the name of the employee")
    name=input()
    f=0
    for i in emp:
        if(i['name']==name):
            print(f"Employee with name:{name} is present")
            print("")
            f=1
            return
    if(f==0):
        print(f"Employee with name:{name} is not present")
        print("")


    
def search_emp_by_city(emp):
    print("Enter the city of the employee")

    city=input()
    f=0
    for i in emp:
        if(i['city']==city):
            print(f"Employee with city name:{city} is present")
            print("")
            f=1
            return
    if(f==0):
        print(f"Employee with city name:{city} is not present")
        print("")


def edit_emp(emp):
    print("Please enter the id of the employee")
    emp_id=(int)(input())
    idx=-1
    for index, i in enumerate(emp):
        if(i['employee_id'] == emp_id):
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
        emp[idx]['name']=name
    print("If you want to change city of the employee , enter YES")
    response=input()
    if(response=='YES'):
        print("Enter city")
        name=input()
        emp[idx]['city']=name
    print("If you want to change salary of the employee , enter YES")
    response=input()
    if(response=='YES'):
        print("Enter salary")
        salary=(float)(input())
        emp[idx]['salary']=salary


def delete_by_id(emp):
    print("Enter the id")
    emp_id=(int)(input())
    for index,value in enumerate(emp):
        if(value["employee_id"]==emp_id):
            del emp[index]
            return
        
    print("Employee not found")
    print("")


def delete_by_name(emp):
    print("Enter the name")
    name=(input())
    for index,value in enumerate(emp):
        if(value["name"]==name):
            del emp[index]
            return   
    print("Employee not found") 
    print("")

def delete_emp(emp):
    print("1:Delete employee on the basis of employee id.")
    print("2:Delete employee on the basis of name.")
    choice=(int)(input())
    if(choice==1):
        delete_by_id(emp)

    else:
        delete_by_name(emp)


emp=[]
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
        continue
    elif(num==1):
        add_new(emp)
    elif(num==2):
        view_emp(emp)
    elif(num==3):
        search_emp(emp)
    elif(num==4):
        edit_emp(emp)
    elif(num==5):
        delete_emp(emp)
    elif(num==6):
        view_name(emp)
    elif(num==7):
        filter_salary(emp)
    elif(num==8):
        total_salary(emp)
    else:
        break


    
