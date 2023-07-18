/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> l1 = new ArrayList<Integer>();
        ArrayList<Integer> l2 = new ArrayList<Integer>();
        dfs(root1, l1);
        dfs(root2, l2);
        return l1.equals(l2);
    }

    public void dfs(TreeNode root, ArrayList<Integer> leaf){
        if(root.left == null && root.right == null){
            leaf.add(root.val);
            return;
        }
        if(root.left != null){
            dfs(root.left, leaf);
        }
        if(root.right != null){
            dfs(root.right, leaf);
        }

    }
}