# Restaurant Tip Calculator 
# Create a program that allows the user to enter the price of a meal at a restaurant. 
# The program calculates the amount of the tip to be paid at 20%. 
# The tip and total price are then displayed separately.

# EXTRA CREDIT
# Ask the user how much percentage they would like to tip?

# DOUBLE EXTRA CREDIT
# Put your script in a Github repository, call it 'Tip Calculator'
#hello 

cost = int(input("how much your meal cost?: "))
print ("Your meal is " + str(cost) + " dollars without tax.")
tip = int(input("What is the tip rate?: "))
print ("You are being tipping " + str(tip) + "%")
tax_variable = (tip / 100)
total = (cost + tip)
print ("Your cost without tip is " + str(cost) + " dollars, but your cost with tip equal to " + str(total) + " dollars.")