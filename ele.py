import sys

if len(sys.argv) != 5:
    print("Usage: python ele.py <product_name> <product_id> <price> <quantity>")
    sys.exit(1)

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
