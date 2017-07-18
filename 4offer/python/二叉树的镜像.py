# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return root;
        left = root.left
        right = root.right
        root.right = self.Mirror(left)
        root.left = self.Mirror(right)
        return root