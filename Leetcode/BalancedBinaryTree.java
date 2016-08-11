/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        } else {
            int leftHeight = 0;
            int rightHeight = 0;
            if (root.left != null) {
                leftHeight = findDepth(root.left);
            }
            if (root.right != null) {
                rightHeight = findDepth(root.right);
            }
            int heightDiff = Math.abs(leftHeight - rightHeight);
            if (leftHeight == -1 || rightHeight == -1 || heightDiff > 1) {
                return false;
            } else {
                return true;
            }
        }
    }

    private int findDepth(TreeNode node) {
        if (node.left == null && node.right == null) {
            return 1;
        } else {
            int leftHeight, rightHeight;
            if (node.right == null) {
                leftHeight = findDepth(node.left);
                if (leftHeight > 1 || leftHeight == -1) {
                    return -1;
                } else {
                    return leftHeight + 1;
                }
            } else if (node.left == null) {
                rightHeight = findDepth(node.right);
                if (rightHeight > 1 || rightHeight == -1) {
                    return -1;
                } else {
                    return rightHeight + 1;
                }
            } else {
                leftHeight = findDepth(node.left);
                rightHeight = findDepth(node.right);
                int heightDiff = Math.abs(leftHeight - rightHeight);
                if (leftHeight == -1 || rightHeight == -1 || heightDiff > 1) {
                    return -1;
                } else {
                    return leftHeight >= rightHeight ? leftHeight + 1 : rightHeight + 1;
                }
            }
        }
    }
}
