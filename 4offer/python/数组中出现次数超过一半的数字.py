# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        num = None
        cnt = 0
        for x in numbers:
            if num == None:
                num = x
                cnt = 1
            elif num == x:
                cnt = cnt + 1
            elif num != x:
                if cnt > 0:
                    cnt = cnt - 1
                else:
                    cnt = 1
                    num = x
        if cnt == 0:
            return 0
        else:
            cnt = 0
            for x in numbers:
                if num == x:
                    cnt += 1
            if cnt * 2 > len(numbers):
                return num
            else:
                return 0;