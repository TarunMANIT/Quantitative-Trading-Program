a = ["IOC", "WIPRO", "ONGC", "COALINDIA", "DRREDDY", "BPCL"]
b = ["BAJAJ", "SUNPHARMA", "UPL", "ITC"]

# Creating new list
c = a+b
print(c)
print("-------")

# Extending the original list
a.extend(b)
print(a)