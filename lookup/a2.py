import os
nl=os.linesep

def solve():
    result=''
    for x in range(0, 3):
        for y in range(0, 3):
            result = result + str(x)
        result = result + nl
    return result
