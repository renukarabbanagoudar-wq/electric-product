product_name = input("Enter Product Name: ")
product_id = input("Enter Product ID: ")
price = float(input("Enter Price of Product: "))
quantity = int(input("Enter Quantity: "))

# Calculation
total_cost = price * quantity

# Output
print("\n----- Electric Product Details -----")
print("Product Name   :", product_name)
print("Product ID     :", product_id)
print("Price          :", price)
print("Quantity       :", quantity)
print("Total Cost     :", total_cost)