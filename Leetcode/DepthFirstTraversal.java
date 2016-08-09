/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class DepthFirstTraversal {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> nodeList = new ArrayList<List<Integer>>();
        if (root != null) {
            nodeList.add(new ArrayList<Integer>());
            nodeList.get(0).add(root.val);
            if (root.left != null) {
                findNodes(nodeList, root.left, 1);
            }
            if (root.right != null) {
                findNodes(nodeList, root.right, 1);
            }
        }
        return nodeList;
    }

    public void findNodes(List<List<Integer>> nodeList, TreeNode node, int depth) {
        if (depth == nodeList.size()) {
            // Make new list for new depth of nodes
            ArrayList<Integer> tempList = new ArrayList<Integer>();
            tempList.add(node.val);
            // Insert at the front of our list of node lists
            nodeList.add(0, tempList);
        } else {
            // Get index of this node's depth list
            int index = nodeList.size() - 1 - depth;
            nodeList.get(index).add(node.val);
        }
        // Call method on both children nodes with 1 greater depth
        if (node.left != null) {
            findNodes(nodeList, node.left, depth + 1);
        }
        if (node.right != null) {
            findNodes(nodeList, node.right, depth + 1);
        }
    }
}
