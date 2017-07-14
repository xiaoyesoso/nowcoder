# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        arr = [0, 1, 2]
        sum = 3
        for x in range(3, number + 1):
            arr.append(sum + 1)
            sum = sum + arr[x]
        return arr[number]