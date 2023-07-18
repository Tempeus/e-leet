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
    private int count = 0;

    public int goodNodes(TreeNode root) {
        ArrayList<Integer> fake_queue = new ArrayList<>();

        dfs(root, fake_queue);
        return count;
    }

    public void dfs(TreeNode root, ArrayList<Integer> queue){
        queue.add(root.val);
        if(root.val >= Collections.max(queue)){
            count ++;
        }    

        if(root.left == null && root.right == null){
            return;
        }

        if(root.left != null){
            dfs(root.left, queue);
            queue.remove(queue.size() - 1);
        }
        
        if(root.right != null){
            dfs(root.right, queue);
            queue.remove(queue.size() - 1);
        }
    }
}