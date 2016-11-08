def pun():
    non_puns = set(["pin", "pins", "pinned", "pinning", "pinner", "pinners"])

    num_tests = int(input())
    for i in range(0, num_tests):
        score = 0
        sentence = [elem for elem in input().split()]
        for word in sentence:
            for j in range(0, len(word) - 3):
                if len(word) >= 3 and word[j:j + 3].lower() == "pin" and word not in non_puns:
                    score += 1
                    break
        print(score)

if __name__ == "__main__":
    pun()
