# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        bg = 0
        size = len(array)
        if size <= 1:
            return []
        ed = size -1

        while ed < size and bg < ed:
            if array[bg] + array[ed] > tsum:
                ed -= 1
            elif array[bg] + array[ed] < tsum:
                ed += 1
                bg += 1
            else:
                return [array[bg],array[ed]]

        return []

