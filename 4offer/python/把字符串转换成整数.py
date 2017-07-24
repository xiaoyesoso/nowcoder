# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0

        t = s
        if s[0] == '+' or s[0] == '-':
            t = s[1:]
        if len(t) == 0:
            return 0

        for x in t:
            if x not in set(['1','2','3','4','5','6','7','8','9','0','+','-']):
                return 0
        return int(s)