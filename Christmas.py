a = 40
b =0
c = 40
print(' '*a+'★')
while b < a-1 and a > 0:
    print(' '*a+'*'+'*'*b)
    a -= 1
    b += 2
for _ in range(4):
    print(' '*(c-1)+'|||')
print(' '*(c-5), '\_@_@_@_/')
