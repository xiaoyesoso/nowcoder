# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        dp = []
        MAX = -1
        for x in array:
            if len(dp) == 0:
                dp.append(array[0])
                MAX = array[0]
            else:
                if dp[len(dp)-1] > 0:
                    val = dp[len(dp)-1] + x
                    if val > MAX:
                        MAX = val
                    dp.append(val)
                else:
                    if x > MAX:
                        MAX = x
                    dp.append(x)
        return MAX
