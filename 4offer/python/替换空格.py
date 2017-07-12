# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = ""
        for c in s:
            new_s = (new_s + c) if c != ' ' else (new_s + "%20")
        return new_s