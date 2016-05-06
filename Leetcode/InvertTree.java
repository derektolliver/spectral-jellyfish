/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class InvertTree {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        } else {
            inversion(root);
            return root;
        }
    }

    public void inversion(TreeNode node) {
        if (node.left != null && node.right != null) {
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            inversion(node.left);
            inversion(node.right);
        } else if (node.left != null) {
            node.right = node.left;
            node.left = null;
            inversion(node.right);
        } else if (node.right != null) {
            node.left = node.right;
            node.right = null;
            inversion(node.left);
        }
    }
}
