# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        if exponent < 0:
            exponent = 0 - exponent
            base = 1 / base
        result = 1.0
        while exponent > 0:
            result = result * base
            exponent = exponent -1
        return result
