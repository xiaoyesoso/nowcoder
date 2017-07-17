# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        arr = [0,1,2]
        for index in range(3,number+1):
            arr.append(arr[index-1]+arr[index-2])
        return arr[number]