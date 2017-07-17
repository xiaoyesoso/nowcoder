# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        size = len(array)
        if size <= 1:
            return array
        p = 0
        while True:
            isFin = True
            for index in range(0,size - p -1):
                if array[index] % 2 == 0 and array[index+1] % 2 == 1:
                    tmp = array[index]
                    array[index] = array[index+1]
                    array[index+1] = tmp
                    isFin = False
            p = p+1
            if isFin:
                break
        return array

