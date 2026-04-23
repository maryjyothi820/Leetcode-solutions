108.convert sorted array to binary search tree
class Solution:
    def sortedArrayToBST(self, nums):
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            
            return node
        
        return build(0, len(nums) - 1)
110.balanced binary tree
class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            if left == -1:
                return -1
            
            right = check(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return check(root) != -1
112.PATHSUM
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        targetSum -= root.val
        
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))