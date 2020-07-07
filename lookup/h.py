import os
nl=os.linesep

def solve():
    result = ''
    for i in range(1, 22):
        if i % 3 != 0:
            result = result + str(i)
        else:
            result = result + 'bee'
        result = result + ' '
    return result
