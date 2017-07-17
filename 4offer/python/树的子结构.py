# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def compare(self,pRoot1, pRoot2):
        if pRoot2.val != pRoot1.val:
            return False
        b = True
        if pRoot1.left != None and pRoot2.left != None:
            b = b and self.compare(pRoot1.left,pRoot2.left)
        if pRoot1.right != None and pRoot2.right != None:
            b = b and self.compare(pRoot1.right,pRoot2.right)

        #if pRoot1.left != None and pRoot2.left == None:
        #    return False
        if pRoot1.left == None and pRoot2.left != None:
            return False
        #if pRoot1.right != None and pRoot2.right == None:
        #    return False
        if pRoot1.right == None and pRoot2.right != None:
            return False

        return b

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None or pRoot1 == None:
            return False
        isTrue = False
        if pRoot1.val == pRoot1.val:
            if(self.compare(pRoot1,pRoot2)):
                return True
        if pRoot1.left != None:
            if self.HasSubtree(pRoot1.left,pRoot2):
                return True
        if pRoot1.right != None:
            if self.HasSubtree(pRoot1.right, pRoot2):
                return True
        return False
