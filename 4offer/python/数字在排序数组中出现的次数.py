# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        bg = 0
        ed = len(data) - 1
        mid = 0
        have = False
        while bg <= ed:
            mid = (bg + ed)/2
            if data[mid] < k:
                bg = mid + 1
            elif data[mid] > k:
                ed = mid -1
            else:
                have = True
                break
        if not have:
            return 0
        
        p = mid
        cnt = 1
        while p -1 >=0 and data[p-1] == k:
            cnt += 1
            p -= 1

        p = mid
        while p +1 < len(data) and data[p+1] == k:
            cnt += 1
            p += 1

        return cnt
