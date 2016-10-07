from collections import deque

# from collections import defaultdict
#
# def answer(m):
#     # Determine which rows are terminal states
#     states = find_states(m)
#
#     # Find fractions for terminals
#     fractions = find_fractions(m, states)
#     print(fractions)
#
#
# def find_states(m):
#     # Find all terminal rows
#     states = []
#     for r in range(0, len(m)):
#         all_zeroes = True
#         for c in m[r]:
#             if c != 0:
#                 all_zeroes = False
#                 break
#         states.append(all_zeroes)
#     return states
#
# def find_fractions(m, states):
#     fractions = set_dict_values(m)
#     for r in range(0 , len(m)):
#         total = 0
#         for v in m[r]:
#             total += v
#         fractions[r] = (m[r][r], total)
#     return fractions
#
# def set_dict_values(m):
#     # Set all rows to (0, 0) tuple
#     fractions = defaultdict()
#     for r in range(0, len(m)):
#         fractions[r] = (0, 0)
#     return fractions

def answer(m):
    nums_and_dens = dict()
    for r in range(0, len(m)):
        if sum(m[r]) == 0:
            nums_and_dens[r] = (0, 0)
    visited = set()
    # states = deque()
    # probabilities = deque()
    #
    # states.appendleft(0)
    # probabilities.appendleft((1,1))
    # curr_prob = (1, 1)
    # while len(states) > 0:
    #     row = states.popleft()
    #     total = sum(m[row])
    #     prob = probabilities.popleft()
    #     curr_prob = (curr_prob[0] * prob[0], curr_prob[1] * prob[1])
    #     print(curr_prob)
    #     if row not in nums_and_dens:
    #         visited.add(row)
    #         for index in range(0, len(m[row])):
    #             if m[row][index] > 0 and index not in visited:
    #                 states.appendleft(index)
    #                 probabilities.appendleft((m[0][index], total))
    #     else:
    #         if nums_and_dens[row] == (0, 0):
    #             nums_and_dens[row] = curr_prob
    #         else:
    #             num = (curr_prob[0] * nums_and_dens[row][1]) + (curr_prob[1] * nums_and_dens[row][0])
    #             denom = curr_prob[1] * nums_and_dens[row][1]
    #             nums_and_dens[row] = (num, denom)
    #
    # result = []
    # for s in nums_and_dens:
    #     result.append(nums_and_dens[s][0])
    # result.append(sum(result))

    def dfs(row, probability):
        total = sum(m[row])
        if total == 0:
            if nums_and_dens[row] == (0, 0):
                nums_and_dens[row] = probability
            else:
                num = (probability[0] * nums_and_dens[row][1]) + (probability[1] * nums_and_dens[row][0])
                denom = probability[1] * nums_and_dens[row][1]
                nums_and_dens[row] = (num, denom)
            return
        visited.add(row)
        for index in range(len(m[row])):
            if m[row][index] > 0 and index not in visited:
                dfs(index, (probability[0] * m[row][index], probability[1] * total))

    dfs(0, (1, 1))
    result = []
    for elem in nums_and_dens:
        result.append(nums_and_dens[elem][0])
    result.append(sum(result))

    return result

# def dfs(row, probability):
#     total = sum(m[row])
#     if total == 0:
#         if nums_and_dens == (0, 0):
#             nums_and_dens[row] = probability
#         else:
#             num = (probability[0] * nums_and_dens[row][1]) + (probability[1] * nums_and_dens[row][0])
#             denom = probability[1] * nums_and_dens[row][1]
#             nums_and_dens[row] = (num, denom)
#         return
#     visited.add(row)
#     for index in range(m[row]):
#         if m[row][index] > 0 and index not in visited:
#             dfs(index, (probability[0] * m[row][index], probability[1] * total))


if __name__ == "__main__":
    test = [
        [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
        [0,0,0,0,0,0],  # s3 is terminal
        [0,0,0,0,0,0],  # s4 is terminal
        [0,0,0,0,0,0]]  # s5 is terminal

    print(answer(test))
