# Generate multiplication table for 11 to 20

# Table of 11
# 11 x 1 = 11
# 11 x 2 = 22
# ..
# ..
# ------------
# Table of 12
# 12 x 1 = 12
# 12 x 2 = 24
# ..
# ..

for n in range(11,21):
    print('Table of', n)
    for i in range(1, 11):
        print(n, 'x', i, '=', n * i)
    print('--------')
