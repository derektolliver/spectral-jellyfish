/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class LevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> nodeList = new ArrayList<List<Integer>>();
        if (root == null) {
            return nodeList;
        } else {
            ArrayList<Integer> tempList = new ArrayList<Integer>();
            tempList.add(root.val);
            nodeList.add(tempList);
            if (root.left != null) {
                fillList(nodeList, root.left, 1);
            }
            if (root.right != null) {
                fillList(nodeList, root.right, 1);
            }
            return nodeList;
        }
    }

    public void fillList(List<List<Integer>> nodeList, TreeNode node, int depth) {
        List<Integer> tempList = new ArrayList<Integer>();
        if (nodeList.size() == depth) {
            tempList.add(node.val);
            nodeList.add(tempList);
        } else {
            tempList = nodeList.get(depth);
            tempList.add(node.val);
        }
        if (node.left != null) {
            fillList(nodeList, node.left, depth + 1);
        }
        if (node.right != null) {
            fillList(nodeList, node.right, depth + 1);
        }
    }
}
