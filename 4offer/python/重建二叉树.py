# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return TreeNode(pre[0])
        index = 0
        while tin[index] != pre[0]:
            index = index +1
        root.left = self.reConstructBinaryTree(pre=pre[1:index+1],tin=tin[0:index])
        root.right = self.reConstructBinaryTree(pre=pre[index+1:],tin=tin[index+1:])
        return root


x = Solution()
tree = x.reConstructBinaryTree(pre=[1,2,3,4,5,6,7],tin=[3,2,4,1,6,5,7])

print(tree)


