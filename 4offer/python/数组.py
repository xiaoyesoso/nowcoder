# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        size1 = len(array)
        size2 = len(array[0])
        i = size1 - 1
        j = 0
        while i >= 0 and j < size2:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False

x = Solution()

b = x.Find(target=11, array=[[1, 2], [10, 19]])
print(b)
