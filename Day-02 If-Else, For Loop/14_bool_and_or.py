_open = 100
_high = 105
_low = 98.3
_close = 105


bullish_condition = _open < _close
super_condition = _high == _close

print(bullish_condition, super_condition)

final_condition = bullish_condition and super_condition
print(final_condition)

f = (_open < _close) and (_high == _close)
print(f)

"""
T and T -> T
T and F -> F
F and T -> F
F and F -> F

T or T -> T
T or F -> T
F or T -> T
F or F -> F
"""

print('------------')
a = 5
b = 6.7
c = 50


print((a > b) and (b > c))
print((a > b) and (b > c) and (b == c))
print((a > b) or (b > c))
print((a > b) or (b < c))

print('------------')

if (a > b) or (b < c):
    print('True in IF')
else:
    print('False in IF')