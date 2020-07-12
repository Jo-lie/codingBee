import os
nl=os.linesep

def solve():
    result = ''
    for x in range(1, 22):
         h = x % 3
         if h == 0:
            result = result + 'bee' + ' '
         else:
            result = result + str(x) + ' '

    #result = result + nl

    return result
print(solve())








