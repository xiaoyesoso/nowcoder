# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        bg = 0
        ed = len(rotateArray) -1
        if ed < 0 :
            return 0
        while(bg < ed):
            mid = (bg + ed)/2
            if mid == bg:
                return rotateArray[bg] if rotateArray[bg] < rotateArray[ed] else rotateArray[ed]
            if rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]
            if rotateArray[mid] > rotateArray[ed]:
                bg = mid+1
            else:
                ed = mid -1
        return rotateArray[ed]