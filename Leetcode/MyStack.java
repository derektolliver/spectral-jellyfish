class MyStack {
    LinkedList<Integer> list = new LinkedList<Integer>();

    // Push element x onto stack.
    public void push(int x) {
        if (list.size() == 0) {
            list.add(x);
        } else {
            LinkedList<Integer> temp = new LinkedList<Integer>();
            while(list.size() != 0) {
                temp.add(list.remove());
            }
            list.add(x);
            while(temp.size() != 0) {
                list.add(temp.remove());
            }
        }
    }

    // Removes the element on top of the stack.
    public void pop() {
        list.remove();
    }

    // Get the top element.
    public int top() {
        return list.peek();
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return list.size() == 0;
    }
}
