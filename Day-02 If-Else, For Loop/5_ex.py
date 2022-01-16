a = ["IOC", "WIPRO", "ONGC", "COALINDIA", "DRREDDY", "BPCL"]
b = ["BAJAJ", "SUNPHARMA", "UPL", "ITC"]

c = a + b

c[0] = c[0].lower()
c[2] = c[2].lower()
c[4] = c[4].lower()
c[6] = c[6].lower()
c[8] = c[8].lower()

print(c)

# for i in range(0, len(c)):
#     if i % 2 != 0:
#         c[i] = c[i].lower()
#
# print(c)
