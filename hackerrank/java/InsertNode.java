/*
  Insert Node at the end of a linked list
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/
    // This is a "method-only" submission.
    // You only need to complete this method.

Node InsertNth(Node head, int data, int position) {
    Node insert = new Node();
    insert.data = data;
    int pos = 0;
    if (position == 0) {
        insert.next = head;
        head = insert;
    } else {
        Node current = head;
        while (current.next != null && pos < position - 1) {
            current = current.next;
            pos++;
        }
        insert.next = current.next;
        current.next = insert;
    }
    return head;
}
