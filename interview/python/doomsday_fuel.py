from collections import defaultdict

def answer(m):
    # Determine which rows are terminal states
    states = find_states(m)

    # Find fractions for terminals
    fractions = find_fractions(m, states)
    print(fractions)


def find_states(m):
    # Find all terminal rows
    states = []
    for r in range(0, len(m)):
        all_zeroes = True
        for c in m[r]:
            if c != 0:
                all_zeroes = False
                break
        states.append(all_zeroes)
    return states

def find_fractions(m, states):
    fractions = set_dict_values(m)
    for r in range(0 , len(m)):
        total = 0
        for v in m[r]:
            total += v
        fractions[r] = (m[r][r], total)
    return fractions

def set_dict_values(m):
    # Set all rows to (0, 0) tuple
    fractions = defaultdict()
    for r in range(0, len(m)):
        fractions[r] = (0, 0)
    return fractions

if __name__ == "__main__":
    test = [
        [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
        [0,0,0,0,0,0],  # s3 is terminal
        [0,0,0,0,0,0],  # s4 is terminal
        [0,0,0,0,0,0]]  # s5 is terminal

    answer(test)
