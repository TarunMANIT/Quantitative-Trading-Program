_open = 100
_close = 98

# write code which prints candle as green or red or grey
# _var1 > _var2
# _var1 == _var2

if _close > _open:
    print('Green candle')
else:
    if _close == _open:
        print('Grey candle')
    else:
        print('Red candle')
