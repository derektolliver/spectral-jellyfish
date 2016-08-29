/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class NthNodeFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode node = dummy;
        int length = 0;
        while (node.next != null) {
            node = node.next;
            length++;
        }
        int remove = length - n;
        node = dummy;
        length = 0;
        while (length < remove) {
            node = node.next;
            length++;
        }
        ListNode nextNode = node.next.next;
        node.next = nextNode;
        return dummy.next;
    }
}
