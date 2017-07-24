# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        size = len(numbers)
        if size == 0:
            return False

        for x in numbers:
            if numbers[x] < 0:
                duplication[0] = numbers[x] + size
                return True
            else:
                numbers[x] = numbers[x] - size

        return False

