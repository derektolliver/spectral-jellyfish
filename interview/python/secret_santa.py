from random import shuffle

def santa(names):
    need_pair = list(names)
    # pairings = {key: none for key in need_pair}
    pairings = dict.fromkeys(need_pair)
    shuffle(need_pair)
    prev_give = ""
    for k, v in pairings:
        if k != need_pair[0]:
            v = need_pair[0]
            prev_give = k
        else:
            if len(count) == 1:
                v = pairings[prev_give]
                pairings[prev_give] = k
            else:
                v = need_pair[1]

if __name__ == "__main__":
    names = []
    santa(names)
