_open = 100
_close = 100

if _close > _open:
    print("Candle is GREEN")
else:
    print("Candle is RED")

"""
if (condition) 
    code
else:
    code
"""

condition = _close > _open
print(condition, type(condition))

# True, False


if True:
    print('This is true')
else:
    print('This is false')

print('-----------')

a = 1
b = 2
c = 3

print(a > b)
print(a > c)
print(a < c)
print(a <= c)
print(a == b)
print(a != b)
