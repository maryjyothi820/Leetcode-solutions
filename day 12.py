98.validate binary serach tree
class Solution:
    def isValidBST(self,root):
        stack = []
        prev = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= prev:
                return False

            prev = root.val
            root = root.right

        return True
124.maximum tree binary path sum
class Solution:
    def maxPathSum(self, root):
        if not root:
            return 0
        
        self.max_sum = float('-inf')   # Global maximum path sum
        
        def dfs(node):
           
            if not node:
                return 0
                        
            left_gain = max(dfs(node.left), 0)   # Ignore negative contribution
            right_gain = max(dfs(node.right), 0)
                  
            current_path = node.val + left_gain + right_gain
                
            self.max_sum = max(self.max_sum, current_path)
                        
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        
        return self.max_sum
129.sum root to leaf numbers
class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        
        def dfs(node, current_number):
            if not node:
                return 0
            
            current_number = current_number * 10 + node.val
            
            if not node.left and not node.right:
                return current_number
            
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)
            
            return left_sum + right_sum
        
        return dfs(root, 0)