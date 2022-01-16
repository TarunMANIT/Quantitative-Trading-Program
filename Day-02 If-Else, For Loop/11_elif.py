# Task
# 1) If close greater than open print Bullish
# 2) If close is high of the day than print Super Bullish
# 3) If close less than open print Bearish
# 4) If close is low of the day than print Super Bearish
# 5) If close equal open then print gray

_open = 100
_high = 100
_low = 100
_close = 100

if _close==_open:
    print("Grey")
elif _close>_open:
    print("Bullish")
elif _clode==_high:
    print("Super Bullish")
elif _close<_open:
    print("Bearish")
elif _close==_low:
    print("Super Bearish")