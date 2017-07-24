# -*- coding:utf-8 -*-
class Solution:

    result = []

    def cal(self,bg,ed):
        return (bg+ed)*(ed - bg +1)/2

    def add(self,bg,ed):
        arr = []
        for x in range(bg,ed+1):
            arr.append(x)
        self.result.append(arr)

    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 1:
            return []
        bg = 1
        ed = 1
        self.result = []
        while bg <= ed and ed <= tsum:
            t = self.cal(bg,ed)
            if t == tsum:
                self.add(bg,ed)
                bg += 1
            elif t < tsum:
                ed += 1
            else:
                ed -= 1
                bg += 1
        return self.result

