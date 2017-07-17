# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        for index in range(0,32):
            if n&(1<<index) != 0:
                cnt = cnt +1
        return cnt
