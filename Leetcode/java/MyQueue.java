public class MyQueue {

    Stack queue = new Stack();

    // Push element x to the back of queue.
    public void push(int x) {
        queue.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        Stack temp = new Stack();
        while (!queue.empty()) {
            temp.push(queue.pop());
        }
        temp.pop();
        while (!temp.empty()) {
            queue.push(temp.pop());
        }
    }

    // Get the front element.
    public int peek() {
        Stack temp = new Stack();
        while (!queue.empty()) {
            temp.push(queue.pop());
        }
        Object result = temp.peek();
        while (!temp.empty()) {
            queue.push(temp.pop());
        }
        return (int) result;
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return queue.empty();
    }
}
