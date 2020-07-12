import os
nl=os.linesep

def solve():
    result = ''
    n = 0
    for x in range(0, 3):
        n = n + 1
        for y in range(3):

            result = result + str(x)
        result = result + nl
    return result


