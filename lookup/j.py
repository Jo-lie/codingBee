import os
nl=os.linesep

now=[0, 1, 1, 0]
last=4

def solve():
    global now
    for n in range(0, last):
        newNow=[0]
        for i in range(0, len(now)-1):
            left =now[i]
            right=now[i+1]
            newNow.append(left+right)
        newNow.append(0)
        now=newNow

    result=''
    for x in range(1, len(newNow)-1):
        result = result + str(newNow[x]) + ' '
    result = result + nl
    return result
