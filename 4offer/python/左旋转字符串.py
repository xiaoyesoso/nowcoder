# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        size = len(s)
        if size <= 0:
            return ""
        n = n % size
        return s[n:] + s[:n]