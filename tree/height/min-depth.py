# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.min_depth = float("inf")

    def minDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.cal(root, 1)
        return self.min_depth

    def cal(self, root, depth):
        if root.left is not None:
            depth += 1
            self.cal(root.left, depth)
            depth -= 1
        if root.right is not None:
            depth += 1
            self.cal(root.right, depth)
            depth -= 1

        if root.right is None and root.left is None:
            self.min_depth = min(self.min_depth, depth)

#lmf
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if (left and right) or (not left and not right):
            return min(left,right) + 1
        # 只有left/right，要按照长的一边算depth
        return left + 1 if left else right + 1