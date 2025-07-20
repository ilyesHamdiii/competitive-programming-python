# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Medium


# Time: O(n)
# Space: O(n)
#Idea: Maintain prefix sums while doing dfs from root to leaf. If currentSum-prefixSum=targetSum, then we've found a #path that has a value of target. If we encountered prefixSum n times, then we've found n such paths.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                count = sums[total-targetSum]

                sums[total] += 1
                count += dfs(root.left, total) + dfs(root.right, total)
                sums[total] -= 1

            return count

        return dfs(root, 0)