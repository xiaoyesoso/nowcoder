# -*- coding:utf-8 -*-
class Solution:
    arr = []
    MIN = 999999
    def push(self, node):
        # write code here
        if node < self.MIN:
            self.MIN = node
        self.arr.append(node)
    def pop(self):
        # write code here
        size = len(self.arr)
        if self.arr[size-1] > self.MIN:
            self.arr.pop()
        else:
            self.arr.pop()
            self.MIN = 999999
            for x in self.arr:
                if x < self.MIN:
                    self.MIN = x
    def top(self):
        # write code here
        return arr[len(self.arr)-1]
    def min(self):
        # write code here
        return self.MIN