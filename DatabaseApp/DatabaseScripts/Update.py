from DatabaseApp.models import Employee, Department

# Update specific value of specific item from Table

Department.objects.filter(departmentKey = 1).update(departmentName = 'hr')

print(Department.objects.filter(departmentKey = 1).values())
# Output: <QuerySet [{'departmentKey': 1, 'departmentName': 'hr'}]>

# To update multiple values from specific item from Table 

hrKey = Department.objects.get(departmentKey = 1)

Employee.objects.filter(department_Key = hrKey, employeeID = 101).update(employeeName = 'Riya', dob = '1996-10-20',employeeEmail ='Riya@imail.com')

print(Employee.objects.filter(department_Key = hrKey, employeeID = 101).values())
# Output: <QuerySet [{'employeeID': 101, 'employeeName': 'Riya', 'dob': datetime.date(1996, 10, 20), 'department_Key_id': 1, 'employeeEmail': 'Riya@imail.com'}]>
