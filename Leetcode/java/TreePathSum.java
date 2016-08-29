/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class TreePathSum {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        } else if (root.left == null && root.right == null) {
            if (root.val == sum) {
                return true;
            } else {
                return false;
            }
        } else {
            boolean sumExists = false;
            if (root.left != null) {
                sumExists = findPathSum(root.left, root.val, sum);
            }
            if (root.right != null && !sumExists) {
                sumExists = findPathSum(root.right, root.val, sum);
            }
            return sumExists;
        }
    }

    public boolean findPathSum(TreeNode node, int currSum, int sum) {
        if (node.left == null && node.right == null) {
            if (currSum + node.val == sum) {
                return true;
            } else {
                return false;
            }
        } else {
            boolean sumExists = false;
            if (node.left != null) {
                sumExists = findPathSum(node.left, currSum + node.val, sum);
            }
            if (node.right != null && !sumExists) {
                sumExists = findPathSum(node.right, currSum + node.val, sum);
            }
            return sumExists;
        }
    }
}
