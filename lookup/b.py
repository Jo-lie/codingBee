import os
nl=os.linesep

def solve():
    result=''
    for x in range(0, 3):
        for y in range(0, 5):
            result = result + str(y)
        result = result + nl
    return result
