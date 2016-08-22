/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class MinTreeDepth {
    public int minDepth(TreeNode root) {
        int depth = 0;
        if (root != null) {
            depth++;
            int currDepth = depth;
            boolean leftChecked = false;
            if (root.left != null) {
                depth = findDepth(root.left, depth + 1);
                leftChecked = true;
            }
            if (root.right != null) {
                int right = findDepth(root.right, currDepth + 1);
                if (!leftChecked || (leftChecked && depth > right)) {
                    depth = right;
                }
            }
        }
        return depth;
    }

    public int findDepth(TreeNode node, int depth) {
        if (node.left == null && node.right == null) {
            return depth;
        } else {
            boolean leftChecked = false;
            int currDepth = depth;
            if (node.left != null) {
                depth = findDepth(node.left, depth + 1);
                leftChecked = true;
            }
            if (node.right != null) {
                int right = findDepth(node.right, currDepth + 1);
                if (!leftChecked || (leftChecked && depth > right)) {
                    depth = right;
                }
            }
            return depth;
        }
    }
}
