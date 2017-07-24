# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:

    def IsBalanced_with_Hight(self,pRoot):
        if pRoot == None:
            return (True,0)
        (is_left,left) = self.IsBalanced_with_Hight(pRoot.left)
        (is_right, right) = self.IsBalanced_with_Hight(pRoot.right)
        return (is_left and is_right and abs(left-right) <=1 ,max(left,right)+1)

    def IsBalanced_Solution(self, pRoot):
        # write code here
        (isB,h) = self.IsBalanced_with_Hight(pRoot)
        return  isB