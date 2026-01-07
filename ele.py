import sys

product_name = sys.argv[1]
product_id = sys.argv[2]
price = float(sys.argv[3])
quantity = int(sys.argv[4])

total_cost = price * quantity

print("----- Electric Product Details -----")
print("Product Name :", product_name)
print("Product ID   :", product_id)
print("Price        :", price)
print("Quantity     :", quantity)
print("Total Cost   :", total_cost)
