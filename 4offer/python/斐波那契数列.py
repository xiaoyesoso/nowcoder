# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        arr = [0,1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for x in range(2,n+1):
            arr.append(arr[x-1] + arr[x-2])
        return arr[n]
