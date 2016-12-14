num_tests = int(input())
for i in range(num_tests):
    tgt_word = input()
    suffix = []
    index = len(tgt_word) - 1
    while index != 0 and tgt_word[index - 1] >= tgt_word[index]:
        index -= 1
    if index == 0:
        print('no answer')
    else:
        pivot, swap = index - 1, len(tgt_word) - 1
        while tgt_word[pivot] >= tgt_word[swap]:
            swap -= 1
        temp = tgt_word[pivot]
        tgt_word = tgt_word[:pivot] + tgt_word[swap] + tgt_word[pivot + 1:]
        tgt_word = tgt_word[:swap] + temp + tgt_word[swap + 1:]
        rev_loops = len(tgt_word) - index
        if len(tgt_word) % 2 == 0:
            rev_loops += 1
        rev_loops //= 2
        for j in range(rev_loops):
            temp = tgt_word[index + j]
            tgt_word = tgt_word[:index + j] + tgt_word[len(tgt_word) - 1 - j] + tgt_word[index + j + 1:]
            tgt_word = tgt_word[:len(tgt_word) - 1 - j] + temp + tgt_word[len(tgt_word) - j:]
        print(tgt_word)
