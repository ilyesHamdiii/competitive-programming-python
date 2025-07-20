# https:https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Medium


# Time: O(n)
# Space: O(n)
""" Approach
Depth-First Search (DFS): Traverse the tree while tracking the current maximum value in the path.
Max Propagation: At each node, update the maximum value encountered so far.
Good Node Check: If the current node's value ≥ current max, count it as good.
Recursive Sum: Sum counts from left and right subtrees.
 """
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            max_val = max(max_val, node.val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            return left + right + (1 if node.val >= max_val else 0)
        
        return dfs(root, float('-inf'))