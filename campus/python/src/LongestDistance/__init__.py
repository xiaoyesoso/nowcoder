# -*- coding:utf-8 -*-

class LongestDistance:
    def getDis(self, A, n):
        # write code here
        return max([A[j] - A[i] for i in range(n) for j in range(i+1,n)])