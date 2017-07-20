# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        ed = 0
        is_true = True
        while ed < len(sequence) and sequence[ed] < root:
            ed = ed + 1
        if 0 != ed-1:
            is_true = is_true and self.VerifySquenceOfBST(sequence[0:ed-1])

        ed2 = ed
        while ed2 < len(sequence):
            if sequence[ed2] < root:
                return False
            ed2 = ed2 + 1

        return is_true and self.VerifySquenceOfBST(sequence[ed:-1]) if ed != len(sequence)-1 else is_true

