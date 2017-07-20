# -*- coding:utf-8 -*-
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    path = []
    pathes = []
    SUM = 0

    def findit(self, root, expectNumber):
        if root == None:
            return []
        self.path.append(root.val)
        self.SUM = self.SUM + root.val
        if root.left != None:
            self.findit(root.left,expectNumber)
        if root.right != None:
            self.findit(root.right,expectNumber)
        if root.left == None and root.right == None and self.SUM == expectNumber:
            self.pathes.append(copy.copy(self.path))
        self.SUM = self.SUM - root.val
        self.path.pop()

    def FindPath(self, root, expectNumber):
        # write code here
        self.path = []
        self.pathes = []
        self.SUM = 0
        self.findit(root,expectNumber)
        return self.pathes

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)

x = Solution()
print(x.FindPath(root,22))