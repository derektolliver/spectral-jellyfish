/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class MergeList {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode node = null;
        if (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                node = l2;
                l2 = l2.next;
            } else {
                node = l1;
                l1 = l1.next;
            }
        }
        while (l1 != null && l2 != null) {
            ListNode node = new ListNode(0);
            if (l1.val > l2.val) {
                node = l2;
                l2 = l2.next;
            } else {
                node = l1;
                l1 = l1.next;
            }
        }
        return node;
    }
}
