/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class LinkedCycle {
    public boolean hasCycle(ListNode head) {
        ListNode node = head;
        HashSet<ListNode> nodeSet = new HashSet<ListNode>();
        while (node != null) {
            if (nodeSet.contains(node)) {
                return true;
            }
            nodeSet.add(node);
            node = node.next;
        }
        return false;
    }
}
