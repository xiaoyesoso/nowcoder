# -*- coding:utf-8 -*-
class Solution:
    stack1 = []
    stack2 = []

    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2) > 0:
            return self.stack2.pop()
        elif len(self.stack1) == 0:
            return None
        else:
            while(len(self.stack1) !=0):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()