import os
nl=os.linesep

def solve():
    result = ''
    number = [1,1,1,1,1,0,1,1,1,1]
    for x in range number:
        for y in range(0,3):
            if x > 1:
                result = 1
            else:
                result = 0
            result = result + str(y)
        return result
