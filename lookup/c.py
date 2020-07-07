import os
nl=os.linesep

def solve():
    result=''
    for x in range(0, 4):
        for y in range(0, 4):
            result = result + str(y)
        result = result + nl
    return result
