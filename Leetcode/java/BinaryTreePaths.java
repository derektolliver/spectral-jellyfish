/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class BinaryTreePaths {
    public List<String> binaryTreePaths(TreeNode root) {
        ArrayList<String> paths = new ArrayList<String>();
        String path = "";

        if (root != null) {
            path += Integer.toString(root.val);
            if (root.left == null && root.right == null) {
                paths.add(path);
            } else {
                if (root.left != null) {
                    pathFinder(root.left, path, paths);
                }
                if (root.right != null) {
                    pathFinder(root.right, path, paths);
                }
            }
        }

        return paths;
    }

    public static void pathFinder(TreeNode node, String currPath, ArrayList<String> paths) {
        currPath += "->";
        currPath += Integer.toString(node.val);
        if (node.left == null && node.right == null) {
            paths.add(currPath);
        } else {
            if (node.left != null) {
                pathFinder(node.left, currPath, paths);
            }
            if (node.right != null) {
                pathFinder(node.right, currPath, paths);
            }
        }
    }
}
