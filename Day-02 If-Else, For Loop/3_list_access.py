nifty50 = ['INFY', "SBIN", 100, "ICICIBANK", "XYZ"]
# index     0       1       2            3

print(nifty50[0])
print(nifty50[1])
print(nifty50[2])
print(nifty50[3])

print(type(nifty50))
print(type(nifty50[1]))
print(type(nifty50[2]))

print('----------')


nifty50.append('WIPRO')
print(nifty50[1])

nifty50.insert(0, 'TCS')
print(nifty50)
print(nifty50[1])

