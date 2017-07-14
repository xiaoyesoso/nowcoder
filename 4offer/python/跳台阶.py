# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        arr = [0,1,2]
        for x in range(3,number+1):
            arr.append(arr[x-1]+arr[x-2])
        return arr[number]