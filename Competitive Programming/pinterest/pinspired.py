def pun():
    non_puns = set(["pin", "pins", "pinned", "pinning", "pinner", "pinners"])

    num_tests = int(input())
    for i in range(0, num_tests):
        score = 0
        sentence = [elem for elem in input().split()]
        for word in sentence:
            if "pin" in word.lower() and word.lower() not in non_puns:
                score += 1
        print(score)

if __name__ == "__main__":
    pun()
