# (i) Write a function which takes principal amount, interest rate and time. This function returns 
# compound interest. Call this function to print the output. 
# (ii) Save this function (as a module) in a python file and call it in another python file.
  

def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)-principal
principal = float(input("Principal: "))
rate = float(input("Rate of interest: "))
time = float(input("Time in years: "))
print("Compound Interest:", compound_interest(principal, rate, time))
# Save this function in a module (e.g., `ci_module.py`) and call it in another file.

    