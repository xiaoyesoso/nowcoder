# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        if num1 == 0:
            return num2
        if num2 == 0:
            return  num1

        if num1 < 0 and num2 > 0  and num1 ^ num2 == num1 << 1:
            return 0

        if num1 > 0 and num2 < 0  and num1 ^ num2 == num2 << 1:
            return 0

        while num2 != 0:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp

        return num1

x = Solution()
x.Add(3,-3)