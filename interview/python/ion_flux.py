def recurse(depth, curr_depth, index, node_list, node_set, node_to_parent):
    if len(node_list) > 0 and curr_depth < depth:
        child_one = recurse(depth, curr_depth + 1, index, node_list, node_set, node_to_parent)
        child_two = recurse(depth, curr_depth + 1, child_one, node_list, node_set, node_to_parent)
        index = child_two + 1
        if child_one in node_set:
            node_to_parent[child_one] = index
        if child_two in node_set:
            node_to_parent[child_two] = index
    else:
        index = index + 1
    return index

def answer(h, q):
    num_nodes = (2 ** h) - 1
    curr_depth = 0
    index = 0
    parent_list = []
    node_set = set()
    for n in q:
        node_set.add(n)
    node_to_parent = dict()
    left_child = recurse(h, curr_depth, index, q, node_set, node_to_parent)
    recurse(h, curr_depth, left_child, q, node_set, node_to_parent)
    if num_nodes in node_to_parent:
        node_to_parent[num_nodes] = -1
    parent_list = []
    for n in range(0, len(q)):
        parent_list.append(node_to_parent[q[n]])
    print(parent_list)

if __name__ == "__main__":
    height = 30
    nodes = [7, 3, 5, 1]
    answer(height, nodes)
