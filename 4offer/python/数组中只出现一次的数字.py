# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) <= 0:
            return []
        all_mix = 0
        for x in array:
            all_mix ^= x

        index = 0
        num = all_mix
        while index < 32 and num & 1 == 0:
            num = num >> 1
            index += 1

        a = 0
        b = 0

        for x in array:
            if (x >> index)&1 == 0:
                a ^= x
            else:
                b ^= x

        return [a,b]
