import os
nl=os.linesep

def solve():
    result = ''
    for x in range(0,3):
        for y in range(0,3):
            if x == 1 and y == 1:
                result = result + str(0)
            else:
                result = result + str(1)
        result = result + nl
    return result
