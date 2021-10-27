#a program that asks a user to enter the total revenue and then prints out the profit made for a company x that makes a profit of 23% of the revenue.

def profit():
    revenue = int(input("Please enter the total revenue:Ksh."))
    
    profit = 0.23 * revenue

    print("The company made a profit of: Ksh.",profit)

profit()

    
