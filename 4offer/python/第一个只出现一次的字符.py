# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        size = len(s)
        if size == 0 :
            return -1
        hash_map = {}
        for id in range(0,size):
            if hash_map.has_key(s[id]):
                hash_map[s[id]] += 1
            else:
                hash_map[s[id]] = 1

        for id in range(0, size):
            if hash_map[s[id]] == 1:
                return id

        return -1