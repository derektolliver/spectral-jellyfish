/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class LinkedListRandom {

    private ArrayList<Integer> map;

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        map = new ArrayList<Integer>();
        ListNode node = head;
        while (node != null) {
            map.add(node.val);
            node = node.next;
        }
    }

    /** Returns a random node's value. */
    public int getRandom() {
        Random r = new Random();
        return map.get(r.nextInt(map.size()));
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
