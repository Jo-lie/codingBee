import os
nl=os.linesep

def solve():
    result=''
    n = 9
    for x in range(0, 3):
        for y in range(0, 3):
            n = n - 1
            result = result + str(n)
        result = result + '\n'
    return result
