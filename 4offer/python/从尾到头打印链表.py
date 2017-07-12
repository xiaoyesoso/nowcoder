# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    arr = []
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode != None:
            self.printListFromTailToHead(listNode.next)
            self.arr.append(listNode.val)
        else:
            self.arr = []
        return self.arr


x = Solution()

node1 = ListNode(67)
node2 = ListNode(0)
node3 = ListNode(24)
node4 = ListNode(58)

node1.next = node2
node2.next = node3
node3.next = node4


print(x.printListFromTailToHead(node1))