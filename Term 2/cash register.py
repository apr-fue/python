# April Fuentes
# Cash Register
# 09/09/19

# Declare & initialize Variables
numItems = input("number of items")
costPerItem = input("cost per item")
taxRate = input("tax rate")

# Calculate and store the sub-total
subTotal = numItems * costPerItem
# Calculate and store the tax amount
taxAmount = subTotal * taxRate
# Calculate and store the total price
totalPrice = subTotal + taxAmount

# Show the full receipt to the screen
print("        SALES RECEIPT")
print("Number of items          " ,numItems, sep=": ")
print("Cost Per Item               ",costPerItem, sep=": $")
print("Tax Rate                       " ,taxRate, sep=": ")
print("Tax Amount                   " ,taxAmount, sep=": $")
print("Total Price                     " ,totalPrice, sep=": $")

input()
