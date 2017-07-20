# -*- coding:utf-8 -*-
class Solution:
    arr = []
    def per(self,ss,bg):
        if bg == len(ss) -1 :
            self.arr.append(ss)
        else:
            for p in range(bg,len(ss)):
                if p == bg or ss[p] != ss[bg]:
                    ll = list(ss)
                    tmp = ll[bg]
                    ll[bg] = ll[p]
                    ll[p] = tmp
                    self.per(''.join(ll),bg+1)

    def Permutation(self, ss):
        # write code here
        self.arr = []
        self.per(ss,0)
        return sorted(self.arr)


x = Solution()
print(x.Permutation('aa'))