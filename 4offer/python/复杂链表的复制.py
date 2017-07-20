# -*- coding:utf-8 -*-
import copy
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    result = RandomListNode(0)
    def Clone(self, pHead):
        # write code here
        self.result = RandomListNode(0)
        if pHead == None:
            return None
        p = pHead
        while p != None:
            q = p.next
            p.next = RandomListNode(p.label)
            p.next.next = q
            p.next.random = p.random
            p = q
        pre = pHead
        self.result = copy.deepcopy(pHead.next)
        p = self.result
        while(pre != None):
            if pre.random != None:
                p.random = pre.random.next
            pre = p.next
            if pre != None:
                p.next = pre.next
            p = p.next
        return self.result