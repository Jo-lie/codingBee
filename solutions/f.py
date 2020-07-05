import os
nl=os.linesep

def solve():
    result=''
    n = 9
    for x in range(0, 3):
        for y in range(0, 3):
            n = n + 1
            h = (n % 2) + 1
            result = result + str(h)
        result = result + nl
    return result
