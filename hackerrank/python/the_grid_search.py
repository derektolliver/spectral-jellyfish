import sys

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

    found = False
    for row in range(len(G)):
        for col in range(len(G[row])):
            if G[row][col] == P[0][0] and (row + len(P)) <= len(G) and (col + len(P[0])) <= len(G[row]):
                not_found = False
                for row_i in range(len(P)):
                    for col_i in range(len(P[row_i])):
                        if G[row + row_i][col + col_i] != P[row_i][col_i]:
                            not_found = True
                            break
                    if not_found:
                        break
                if not not_found:
                    found = True
            if found:
                break
        if found:
            break
    if found:
        print("YES")
    else:
        print("NO")
