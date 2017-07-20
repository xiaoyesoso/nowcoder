# -*- coding:utf-8 -*-
class Solution:
    arr = []
    def IsPopOrder(self, pushV, popV):
        # write code here
        self.arr = []
        size = len(pushV)
        if size == 0:
            return True
        p_index = 0
        for x in popV:
            if len(self.arr) == 0:
                while p_index < size and pushV[p_index] != x:
                    self.arr.append(pushV[p_index])
                    p_index = p_index + 1
                if p_index == size :
                    return False
                else:
                    p_index = p_index +1
            else:
                if self.arr[len(self.arr)-1] == x:
                    self.arr.pop()
                else:
                    while p_index < size and pushV[p_index] != x:
                        self.arr.append(pushV[p_index])
                        p_index = p_index + 1
                    if p_index == size:
                        return False
                    else:
                        p_index = p_index + 1
        if len(self.arr) > 0:
            return False
        else:
            return True


x = Solution()

print (x.IsPopOrder([1],[1]))