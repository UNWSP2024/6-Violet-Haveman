# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
def salesTax():
    sales = float(input("Total Sales from Past Month: "))
    county = 0.025
    state = 0.05
    countytax = sales*county
    statetax = state*sales
    total = countytax+statetax
    sales_tax = total + sales
    print ("Total County Sales Tax: $", countytax)
    print ("Total State Sales Tax: $", statetax)
    print ("Total Sales Tax: $", total)
    print("Total Sales plus Tax: $", sales_tax)
    return salesTax()
salesTax()