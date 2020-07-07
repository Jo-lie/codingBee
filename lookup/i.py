import os
nl=os.linesep

#           [0, 1, 0]
now=       [0, 1, 1, 0]
#newNow=  [0, 1, 2, 1, 0]

def solve():
    global now
    result = '1 ' + nl + '1 1 ' + nl
    for n in range(0, 3):
        newNow=[0]
        for i in range(0, len(now)-1):
            left =now[i]
            right=now[i+1]
            newNow.append(left+right)
        newNow.append(0)
        for x in range(1, len(newNow)-1):
            result = result + str(newNow[x]) + ' '
        result = result + nl
        now=newNow
    return result
