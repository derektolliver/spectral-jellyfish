/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class TreeEquality {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p == null || q == null) {
            return false;
        } else {
            return checkEquality(p, q);
        }
    }

    public boolean checkEquality(TreeNode p, TreeNode q) {
        boolean equality = false;
        if (p.val == q.val) {
            equality = true;
        }
        if (equality) {
            if (p.left == null && p.right == null && q.right == null && q.left == null) {
                return true;
            } else if (p.left == null && q.left == null) {
                return checkEquality(p.right, q.right);
            } else if (p.right == null && q.right == null) {
                return checkEquality(p.left, q.left);
            } else if (p.left != null && p.right != null && q.right != null && q.left != null) {
                equality = checkEquality(p.left, q.left) && checkEquality(p.right, q.right);
                return equality;
            }
        }
        return false;
    }
}
