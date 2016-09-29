from collections import defaultdict

def answer(l):
    buckets = defaultdict(list)
    for x in l:
        if x % 3 == 0:
            buckets[0].append(x)
        elif x % 3 == 1:
            buckets[1].append(x)
        else:
            buckets[2].append(x)
    buckets[1].sort(reverse = True)
    buckets[2].sort(reverse = True)

    # Add elements to main bucket
    buckets[0].extend(buckets[1][0 : len(buckets[1]) - (len(buckets[1]) % 3)])
    buckets[0].extend(buckets[2][0 : len(buckets[2]) - (len(buckets[2]) % 3)])

    # Remove elements from old bucket
    buckets[1] = buckets[1][len(buckets[1]) - (len(buckets[1]) % 3):]
    buckets[2] = buckets[2][len(buckets[2]) - (len(buckets[2]) % 3):]

    while len(buckets[1]) > 0 and len(buckets[2]) > 0:
        buckets[0].append(buckets[1].pop(0))
        buckets[0].append(buckets[2].pop(0))

    buckets[0].sort(reverse = True)

    if len(buckets[0]) > 0:
        result_string = ""
        for x in buckets[0]:
            result_string += str(x)
        result = int(result_string)
        return result
    return 0


if __name__ == "__main__":
    num_list = [3, 1, 4, 1, 5, 9]
    print(answer(num_list))
