# -*- coding:utf-8 -*-

class Solution:
    def FindKthToTail(self, head, k):
        ktemp = k
        pre_head = head
        while ktemp > 0 and pre_head != None:
            pre_head = pre_head.next
            ktemp = ktemp -1
            
        if ktemp != 0:
            return None
        result = head
        while pre_head != None:
            pre_head = pre_head.next
            result = result.next
        return  result

