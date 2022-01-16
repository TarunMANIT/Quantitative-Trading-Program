# Take a two numbers from user
# Then print all possible arithmetic operations on it
# +, -, /, *, pow, max value, min value

a = float(input("Enter Number-01: "))
b = float(input("Enter Numbet-02: "))

print(a, '+', b, '=', a+b)
print(a, '-', b, '=', a-b)
print(a, '/', b, '=', a/b)
print(a, '*', b, '=', a*b)
print(a, '^', b, '=', pow(a,b))
print('Max', '=', max(a,b))
print('Min', '=', min(a,b))