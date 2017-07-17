# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        if pHead1 == None:
            return pHead2
        
        if pHead2 == None:
            return pHead1

        result = None
        p =None
        if pHead1.val < pHead2.val:
            result = pHead1
            p = pHead1
            pHead1 = pHead1.next
        else:
            result = pHead2
            p = pHead2
            pHead2 = pHead2.next
        while pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                result.next = pHead1
                result = result.next
                pHead1 = pHead1.next
            else:
                result.next = pHead2
                result = result.next
                pHead2 = pHead2.next

        if pHead1 != None:
            result.next = pHead1
        else:
            result.next = pHead2
        return  p