# -*- coding:utf-8 -*-
import heapq
class Solution:
    arr = []
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k <=0:
            return []
        self.arr = []
        for x in tinput:
            if len(self.arr) < k:
                heapq.heappush(self.arr,-x)
            else:
                if -x > self.arr[0]:
                    heapq.heapreplace(self.arr,-x)
        for index in range(0,len(self.arr)):
            self.arr[index] = -self.arr[index]

        return sorted(self.arr)
