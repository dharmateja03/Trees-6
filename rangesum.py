#TimeComplexity:O(n)
# SpaceCompelxity:O(1)
# Approach:
# Worst case you need to visit allnode but avg time complexit can be improved by tarversing tthrough nodes wich are inrange by using BST prop






class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            left_sum=0
            right_sum=0
            if low <= node.val <= high:
                current_val = node.val
            if node.val>low:
                left_sum = dfs(node.left)
            if node.val<high:
                right_sum = dfs(node.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)
