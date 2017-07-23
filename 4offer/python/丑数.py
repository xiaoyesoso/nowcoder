# -*- coding:utf-8 -*-
import math
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        if index == 1:
            return 1
        arr = [1]
        p2 = 0
        p3 = 0
        p5 = 0

        for id in range(1,index):
            arr.append(min(arr[p2]*2,arr[p3]*3,arr[p5]*5))
            while arr[p2] * 2 <= arr[id]:
                p2 += 1
            while arr[p3] * 3 <= arr[id]:
                p3 += 1
            while arr[p5] * 5 <= arr[id]:
                p5 += 1

        return arr[index-1]

