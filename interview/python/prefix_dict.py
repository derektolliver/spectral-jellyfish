class Node(object):
    def __init__(self, char, following):
        self.val = char
        self.next_nodes = following
        self.last = False

    def get_following(self):
        return self.next_nodes

    def get_node(self, val):
        return self.next_nodes[val]

    def last_val(self):
        return self.last

    def set_last(self):
        self.last = True

def setup(dictionary):
    n = Node("%", set())
    current = n
    for d in dictionary:
        for l in d:
            if l in n.get_following():
                current = n.get_node(l)
            else:
                new_node = Node(l, set())
                current.get_following.add(new_node)
                current = new_node
        current.set_last()
        current = n
    return n

def is_member(curr_node, word):
    if len(word) == 0 and curr_node.last_val() == True:
        return True
    else:
        if word[0] == ".":
            for node in curr_node.get_following():
                possible = is_member(node, word[1:])
                if possible:
                    return True
        else:
            if word[0] in curr_node.get_following():
                return is_member(curr_node.get_node(word[0]), word[1:])
        return False

if __name__ == "__main__":
    dictionary = ["foo", "foobar", "fox", "bar"]
    start_node = setup(dictionary)
    is_member(start_node, "fo")
