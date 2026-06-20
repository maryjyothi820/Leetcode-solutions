701. Insert into a Binary Search Tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root, val):
        # If the tree is empty, create and return the new node
        if not root:
            return TreeNode(val)
        
        # If value is greater, insert into the right subtree
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # If value is smaller, insert into the left subtree
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        return root
