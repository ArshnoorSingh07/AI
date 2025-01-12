# Write a Python Program to input basic salary of an employee and calculate its Gross salary 
# according to following: Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000 
# : HRA = 25%, DA = 90% Basic Salary > 20000 : HRA = 30%, DA = 95%.


basic_sal=float(input("Enter the basic salary: "))
if basic_sal<=10000:
    HRA=0.20*basic_sal
    DA=0.80*basic_sal
elif basic_sal<=20000:
    HRA=0.25*basic_sal
    DA=0.90*basic_sal
else:
    HRA=0.30*basic_sal
    DA=0.9*basic_sal
gross_salary=basic_sal + HRA + DA
print(f"Gross Salary: {gross_salary:.2f}")
