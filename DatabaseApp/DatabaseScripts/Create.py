from DatabaseApp.models import Department, Employee

# Creating entities in Department table
hrKey = Department.objects.get(departmentKey = 1,departmentName = 'HR')
print(hrKey.departmentName, " is created.")
marketKey = Department.objects.get(departmentKey = 2,departmentName = 'Marketing')
print(marketKey.departmentName, " is created.")
finKey = Department.objects.get(departmentKey = 3,departmentName = 'Finance')
print(finKey.departmentName, " is created.")

# Creating entities in Employee table
e1 = Employee.objects.create(employeeID = 101,employeeName = 'Neha', dob = '1996-01-01',
                        department_Key = hrKey, employeeEmail = 'Neha@imail.com')
print(e1.employeeName, ' is created from ',hrKey.departmentName, ' department.')

e2 = Employee.objects.create(employeeID = 102,employeeName = 'Ramesh', dob = '1993-01-01',
                        department_Key = hrKey, employeeEmail = 'Ramesh@imail.com')
print(e2.employeeName, ' is created from ',hrKey.departmentName, ' department.')

e3 = Employee.objects.create(employeeID = 103,employeeName = 'Suresh', dob = '1992-01-01',
                        department_Key = marketKey, employeeEmail = 'Suresh@imail.com')
print(e3.employeeName, ' is created from ',marketKey.departmentName, ' department.')

e4 = Employee.objects.create(employeeID = 104,employeeName = 'Priyanka', dob = '1997-01-01',
                        department_Key = marketKey, employeeEmail = 'Priyanka@imail.com')
print(e4.employeeName, ' is created from ',marketKey.departmentName, ' department.')

e5 = Employee.objects.create(employeeID = 105,employeeName = 'Sachin', dob = '1990-01-01',
                        department_Key = finKey, employeeEmail = 'Sachin@imail.com')
print(e5.employeeName, ' is created from ',finKey.departmentName, ' department.')