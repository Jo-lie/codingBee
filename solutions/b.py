import os
nl=os.linesep

def solve():
    result =''
    n = 0
    for x in range(0,3):
        for y in range(5):
            n = n + 1
            result = result + str(y)
        result = result + nl

    return result
