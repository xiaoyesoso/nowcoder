# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        size = len(numbers)
        if size !=5 :
            return False
        numbers.sort()
        num_of_king = 0
        index = 0
        while numbers[index] == 0:
            num_of_king += 1
            index += 1
        bg = numbers[index]
        while index < size:
            if numbers[index] == bg:
                index += 1
                bg += 1
            else:
                if num_of_king == 0:
                    return False
                num_of_king -= 1
                bg += 1

        return True


x = Solution()
print(x.IsContinuous([1,3,2,5,4]))