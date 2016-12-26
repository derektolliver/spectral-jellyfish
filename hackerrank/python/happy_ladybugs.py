import sys

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    if "_" in b:
        colors = [0] * 26
        for i in b:
            if i != "_":
                letter = ord(i) - 65
                colors[letter] += 1
        for c in colors:
            if c == 1:
                print("NO")
                break
        else:
            print("YES")
    else:
        if n > 1 and b[0] == b[1] and b[len(b) - 1] == b[len(b) - 2]:
            for i in range(1, len(b) - 1):
                if b[i - 1] != b[i] and b[i] != b[i + 1]:
                    print("NO")
                    break
            else:
                print("YES")
        else:
            print("NO")
