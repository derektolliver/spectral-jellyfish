"""
T's path -> path out
N E S W -> E N W S
N E W -> S
N E N W S -> N E S W S
"""
(E(EW)(EW)W)
*WWWW
EEEEN

[ ][ ][E][S]
[ ][*][N,W][W]
[ ][ ][ ][ ]

N E W

S

W E N

def path(to_path):
    if len(to_path) == 0:
        return []
    back_path = [opposite(to_path[0])]
    previous = opposite(to_path[0])
    for i in range(1, len(to_path)):
        if previous == to_path[i]:
            back_path.remove(len(back_path) - 1)
            previous = back_path[len(back_path) - 1]
        else:
            back_path.append(opposite(to_path[i]))
    return rev(back_path)

def opposite(d):
    if (d == 'N'):
        return 'S'
    elif (d == 'S'):
        return 'N'
    elif (d == 'W'):
        return 'E'
    else:
        return 'W'
