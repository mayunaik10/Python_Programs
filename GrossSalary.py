#Q3.Calculate and display gross salary of two categories of employees, permanent and temporary.
#For permanent - gross salary = net salary + Bonus of 15% of net salary, no bonus for temporary employee
def cal(basic):
   pe = basic + (basic*(15/100))  
   return pe 
basic = int(input("Enter Basic Salary: "))
print("Gross Salary for Temporary employee : ",basic)
print("Gross Salary for Permanent employee : ",cal(basic))