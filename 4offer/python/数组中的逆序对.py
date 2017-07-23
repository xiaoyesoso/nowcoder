# -*- coding:utf-8 -*-
import copy
class Solution:

    copy_data = []

    def InverseMerge(self,data,bg,ed):
        if bg >= ed:
            return 0

        size = (ed - bg)/2
        i = bg + size
        j = ed
        cnt = 0

        left = self.InverseMerge(data,bg,bg + size)
        right = self.InverseMerge(data,bg + size +1,ed)
        copy_index = ed
        while i >= bg and j >= bg + size +1:
            if data[i] > data[j]:
                self.copy_data[copy_index] = data[i]
                copy_index -= 1
                i -= 1
                cnt += j - bg - size
            else:
                self.copy_data[copy_index] = data[j]
                copy_index -= 1
                j -= 1

        while i >= bg:
            self.copy_data[copy_index] = data[i]
            copy_index -= 1
            i -= 1

        while j >= bg +size +1:
            self.copy_data[copy_index] = data[j]
            copy_index -= 1
            j -= 1

        for id in range(bg,ed+1):
            data[id] = self.copy_data[id]

        return (left + cnt + right)%1000000007


    def InversePairs(self, data):
        if len(data) == 0:
            return 0
        self.copy_data = copy.deepcopy(data)
        return  self.InverseMerge(data,0,len(data)-1)


x = Solution()
print(x.InversePairs([1,2,3,4,5,6,7,0]))