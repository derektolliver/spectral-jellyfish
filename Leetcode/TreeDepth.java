/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class TreeDepth {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else if (root.left == null && root.right == null) {
            return 1;
        } else if (root.left == null) {
            return findMax(root.right, 1);
        } else if (root.right == null) {
            return findMax(root.left, 1);
        } else {
            return Math.max(findMax(root.left, 1), findMax(root.right, 1));
        }
    }

    public int findMax(TreeNode node, int depth) {
        int newDepth = depth + 1;
        if (node.left == null && node.right == null) {
            // Leaf found
            return newDepth;
        } else {
            if (node.left == null) {
                return findMax(node.right, newDepth);
            } else if (node.right == null) {
                return findMax(node.left, newDepth);
            } else {
                return Math.max(findMax(node.left, newDepth), findMax(node.right, newDepth));
            }
        }
    }
}
