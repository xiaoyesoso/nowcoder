# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        size1 = 0
        p1 = pHead1
        while p1 != None:
            size1 += 1
            p1 = p1.next

        size2 = 0
        p2 = pHead2
        while p2 != None:
            size2 += 1
            p2 = p2.next

        dis = 0

        if size1 < size2:
            p1 = pHead2
            p2 = pHead1
            dis = size2 - size1
        else:
            p1 = pHead1
            p2 = pHead2
            dis = size1 - size2

        while dis != 0:
            p1 = p1.next
            dis -= 1

        while p1 != None and p1.val != p2.val:
            p1 = p1.next
            p2 = p2.next

        return  p1