# -*- coding:utf-8 -*-
import math
class Solution:

    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        if n >0 and n < 9:
            return 1
        str_num = str(n)
        size = len(str_num)
        if size <= 0:
            return 0

        first_num = int(str_num[0])
        First = 0
        if first_num > 1:
            First = math.pow(10,size-1)
        elif first_num ==1:
            ss = str_num[1:]
            First = int(ss) +1

        Other = first_num * (size-1) * math.pow(10,size-2)

        Recursive = self.NumberOf1Between1AndN_Solution(int(str_num[1:])) if size > 1 else 0

        return int(First + Other + Recursive)

x = Solution()
print(x.NumberOf1Between1AndN_Solution(10))