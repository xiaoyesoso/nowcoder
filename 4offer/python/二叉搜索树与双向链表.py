# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution:
    pLast = None
    def ConvertNode(self,pRootOfTree):
        if pRootOfTree == None:
            return
        p = pRootOfTree

        if p.left != None:
            self.ConvertNode(p.left)

        p.left = self.pLast

        if self.pLast != None:
            self.pLast.right = p

        self.pLast = p

        if p.right != None:
            self.ConvertNode(p.right)

    def Convert(self, pRootOfTree):
        # write code here
        self.pLast = None
        copy_root = copy.deepcopy(pRootOfTree)
        self.ConvertNode(copy_root)

        pFirst = self.pLast

        while pFirst != None and pFirst.left != None:
            pFirst = pFirst.left

        return pFirst
