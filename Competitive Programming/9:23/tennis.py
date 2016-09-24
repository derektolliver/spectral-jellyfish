def tennis():
    num_tests = int(input())
    for t in range(num_tests):
        info = [elem for elem in input().split()]
        num_plays = int(info[0])
        p1 = info[1]
        p2 = info[2]
        s1 = 0
        s2 = 0
        for p in range(num_plays):
            winner = input()
            if winner == p1:
                if (s1 == 40 and s2 < 40) or s1 == 41:
                    break
                elif s1 == 0 or s1 == 15:
                    s1 = s1 + 15
                elif s1 == 30:
                    s1 = 40
                elif s1 == 40:
                    if s2 == 41:
                        s2 = 40
                    else:
                        s1 = 41
            else:
                if (s2 == 40 and s1 < 40) or s2 == 41:
                    break
                elif s2 == 0 or s2 == 15:
                    s2 = s2 + 15
                elif s2 == 30:
                    s2 = 40
                elif s2 == 40:
                    if s1 == 41:
                        s1 = 40
                    else:
                        s2 = 41
            if s1 >= 40 and s2 >= 40:
                if s1 != s2:
                    print("advantage " + winner)
                else:
                    print("deuce")
            else:
                if s1 == s2:
                    print(str(s1) + " all")
                else:
                    result = ""
                    if (s1 == 0):
                        result = result + "love"
                    else:
                        result = result + str(s1)
                    result = result + " "
                    if (s2 == 0):
                        result = result + "love"
                    else:
                        result = result + str(s2)
                    print(result)
        if s1 > s2:
            print(p1 + " won!")
        else:
            print(p2 + " won!")

if __name__ == "__main__":
    tennis()
