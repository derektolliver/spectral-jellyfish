def answer(l):
    count = 0
    for i in range(1, len(l) - 1):
        left = []
        right = []
        for j in range(0, i):
            if l[i] % l[j] == 0:
                left.append(l[j])
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                right.append(l[j])
        count += len(left) * len(right)

    return count


if __name__ == "__main__":
    test = [5, 5, 5, 5, 5]
    print(answer(test))

"""
Drafts:

def answer(l):
    num_list = set()
    triples = set()
    for num in l:
        for stack in num_list.copy():
            if num % stack[len(stack) - 1] == 0:
                temp_list = list(stack)
                temp_list.append(num)
                temp_tup = tuple(temp_list)
                if len(temp_tup) == 3 and temp_tup not in triples:
                    triples.add(temp_tup)
                else:
                    num_list.add(temp_tup)
        new_tup = (num,)
        num_list.add(new_tup)

    return len(triples)

-----------------------

from collections import defaultdict

def fill_maps(l, factors_to_divisor, divisor_to_factors, freqs):
    for i in range(0, len(l)):
        freqs[l[i]] += 1
        if l[i] not in factors_to_divisor:
            factors_to_divisor[l[i]] = set()
        for j in range(i + 1, len(l)):
            if l[j] not in divisor_to_factors:
                divisor_to_factors[l[j]] = set()
            if l[j] % l[i] == 0 and l[j] != l[i]:
                factors_to_divisor[l[i]].add(l[j])
                divisor_to_factors[l[j]].add(l[i])

def answer(l):
    factors_to_divisor = dict()
    divisor_to_factors = dict()
    freqs = defaultdict(int)
    fill_maps(l, factors_to_divisor, divisor_to_factors, freqs)
    print(factors_to_divisor)
    print(divisor_to_factors)

    count = 0
    for f in factors_to_divisor:
        divisors = factors_to_divisor[f]
        for v in divisors:
            div_of_div = factors_to_divisor[v]
            count += len(div_of_div)
        if freqs[f] >= 2:
            print(count)
            count += len(factors_to_divisor[f]) + len(divisor_to_factors[f])
            if freqs[f] == 3:
                count += 1

    return count
"""
