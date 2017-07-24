# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        arr = []
        size = len(s)
        if size == 0:
            return ""
        arr = s.split(' ')
        size = len(arr)
        ss = ""
        for x in range(size-1,-1,-1):
            ss = ss + arr[x] if x == size -1 else ss + " " + arr[x]
        return ss
