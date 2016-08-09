/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class TreeSymmetry {
    public boolean isSymmetric(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) {
            // root is null or no children
            return true;
        } else {
            return findSymmetry(root.left, root.right);
        }
    }

    private boolean findSymmetry(TreeNode first, TreeNode second) {
        if (first == null && second == null) {
            // leaves passed
            return true;
        } else if ((first != null && second == null) || (first == null && second != null) || (first.val != second.val)) {
            return false;
        } else {
            // both nodes exist and are equal
            boolean symmetric = findSymmetry(first.left, second.right) && findSymmetry(first.right, second.left);
            return symmetric;
        }
    }
}
