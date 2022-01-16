stock_name = 'INFY'
_open = 101
_close = 103

#PCT change of INFY is X%

x = 100*((-close - _open) / _open)

print("PCT Change of "+stock_name+" is "+str(x)+"%")