import os
nl=os.linesep
#1
def pascal_triangle(n):
    trow = [1]
    y =[0]
    for x in range(max(n,0)):
        result = result + trow
        trow=[1+r for 1, r in zip(trow+y, y+trow)]
    return n>=1
    result = result + n1
    pascal_triangle(5)

#2
def solve():
    result=''
    n = 5
    a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i-1],[j-1]+a[i-1][j])
        if n!= 0:
            a[i].append(1)
for i in range(n):
    result = result + str(' '*(n-i), end='', sep='')
    for j in range(0, i+1):
        result = result + str('{0:6}', format(a[i][j]), end='', sep='')
        result = result + nl


