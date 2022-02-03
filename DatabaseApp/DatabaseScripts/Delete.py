from DatabaseApp.models import Employee, Department

# Delete specific value of specific item from table

hrKey = Department.objects.get(departmentKey = 1)

Employee.objects.filter(department_Key = hrKey, employeeID = 102).delete()

print(Employee.objects.filter(department_Key = hrKey).values())
# Output: <QuerySet [{'employeeID': 101, 'employeeName': 'Riya', 'dob': datetime.date(1996, 10, 20), 'department_Key_id': 1, 'employeeEmail': 'Riya@imail.com'}]>

# Delete all entries from specific item from table

financeKey = Department.objects.get(departmentName = 'Finance')

Employee.objects.filter(department_Key = financeKey).delete()
print(Employee.objects.filter(department_Key = financeKey).values())
# Output: <QuerySet []>

# Delete all entries from table

Employee.objects.all().delete()
print(Employee.objects.values())
# Output: <QuerySet []>