/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        if (head != null) {
            head = reversal(head, null);
        }
        return head;
    }

    public ListNode reversal(ListNode node, ListNode prev) {
        ListNode last = null;
        if (node.next == null) {
            node.next = prev;
            return node;
        } else {
            last = reversal(node.next, node);
            node.next = prev;
        }
        return last;
    }
}
