from DatabaseApp.models import Employee,Department

# To get all values from table Department
departmentValues = Department.objects.values()
print(departmentValues) 
# Output: <QuerySet [{'departmentKey': 1, 'departmentName': 'HR'}, {'departmentKey': 2, 'departmentName': 'Marketing'}, {'departmentKey': 3, 'departmentName': 'Finance'}]>

# To get all values of specific item from table

hrvalues = Department.objects.filter(departmentName = 'HR').values()
print(hrvalues)
# Output: <QuerySet [{'departmentKey': 1, 'departmentName': 'HR'}]>

# To get specific value from specific item from table

hrDepartmentKey = Department.objects.get(departmentName = 'HR').departmentKey
print(hrDepartmentKey)
# Output: 1

# To get object instance

hrObject = Department.objects.get(departmentName = 'HR')
print(hrObject)
# Output: Department object (1)

# We can access any value from object instance

print(hrObject.departmentKey)
# Output: 1
print(hrObject.departmentName)
# Output: HR


## To access table value using foreignKey of another table

hrEmployees = Employee.objects.filter(department_Key = hrObject.departmentKey).values()
print(hrEmployees)
# Output: <QuerySet [{'employeeID': 101, 'employeeName': 'Neha', 'dob': datetime.date(1996, 1, 1), 'department_Key_id': 1, 'employeeEmail': 'Neha@imail.com'}, {'employeeID': 102, 'employeeName': 'Ramesh', 'dob': datetime.date(1993, 1, 1), 'department_Key_id': 1, 'employeeEmail': 'Ramesh@imail.com'}]>


# To apply double filter we can use

rameshValues = Employee.objects.filter(department_Key = hrObject.departmentKey, employeeName = 'Ramesh').values()
print(rameshValues)
# Output: <QuerySet [{'employeeID': 102, 'employeeName': 'Ramesh', 'dob': datetime.date(1993, 1, 1), 'department_Key_id': 1, 'employeeEmail': 'Ramesh@imail.com'}]>