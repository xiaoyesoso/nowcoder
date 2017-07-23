# -*- coding:utf-8 -*-
class Solution:
    def my_cmp(self,x, y):
        if int(x+y) < int(y+x):
            return -1
        elif int(x+y) > int(y+x):
            return 1
        else:
            return 0
    def PrintMinNumber(self, numbers):
        # write code here
        size = len(numbers)
        if size <= 0:
            return ""
        for index in range(0,size):
            numbers[index] = str(numbers[index])
        numbers.sort(self.my_cmp)
        num_str = ""
        for num in numbers:
            num_str += num
        return int(num_str)

x = Solution()
print(x.PrintMinNumber([3,5,1,4,2]))