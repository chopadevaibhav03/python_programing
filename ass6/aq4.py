# Create a function showEmployee() in such a way that it should accept employee name,
# and it’s salary and display both, and if the salary is missing in function call it should show it as 9000

def showEmployee(e_name, e_salary=9000):
    print('Employee name: %s, salary: %s ' % (e_name, e_salary))


showEmployee('Shoeb', 28000)
showEmployee('Rakesh')
