/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class LinkedListsIntersection {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode node1 = headA;
        ListNode node2 = headB;
        if (node1 == null || node2 == null) {
            return null;
        }
        while (node1 != null && node2 != null) {
            if (node1.val < node2.val) {
                node1 = node1.next;
            } else if (node1.val > node2.val) {
                node2 = node2.next;
            } else if (node1.val == node2.val) {
                return node1;
            }
        }
        return null;
    }
}
