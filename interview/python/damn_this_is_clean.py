def recurse(tgt, curr_val, curr_height, side, parent_list):
    if tgt == curr_val:
        if side == 1:
            parent_list.append(tgt + (2 ** (curr_height)))
        elif side == 2:
            parent_list.append(tgt + 1)
        else:
            parent_list.append(-1)
    else:
        poss_left = curr_val - (2 ** (curr_height - 1))
        poss_right = curr_val - 1
        if poss_left >= tgt:
            recurse(tgt, poss_left, curr_height - 1, 1, parent_list)
        else:
            recurse(tgt, poss_right, curr_height - 1, 2, parent_list)

def answer(h, q):
    num_nodes = (2 ** h) - 1
    parent_list = []
    curr_height = h
    for n in q:
        recurse(n, num_nodes, h, 0, parent_list)
    return parent_list
    
