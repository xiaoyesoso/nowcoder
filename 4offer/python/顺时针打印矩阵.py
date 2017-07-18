# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def right(self,x,y,n,matrix,arr):
        for i in range(1,n+1):
            arr.append(matrix[y][x+i])
        return (x+n,y)

    def left(self, x, y, n, matrix, arr):
        for i in range(1, n + 1):
            arr.append(matrix[y][x - i])
        return (x-n,y)

    def up(self, x, y, n, matrix, arr):
        for i in range(1, n + 1):
            arr.append(matrix[y - i][x])
        return (x,y-n)

    def down(self, x, y, n, matrix, arr):
        for i in range(1, n + 1):
            arr.append(matrix[y + i][x])
        return (x,y+n)

    def printMatrix(self, matrix):
        # write code here
        w = len(matrix[0])
        l = len(matrix)
        arr = []
        (x,y) = self.right(-1,0,w,matrix,arr)
        while l > 0 and w > 0:
            l = l -1
            if l > 0:
                (x,y) = self.down(x,y,l,matrix,arr)
            else:
                break
            w = w - 1
            if w > 0:
                (x,y) = self.left(x,y,w,matrix,arr)
            else:
                break
            l = l - 1
            if l > 0:
                (x, y) = self.up(x, y, l, matrix, arr)
            else:
                break
            w = w -1
            if w > 0:
                (x, y) = self.right(x, y, w, matrix, arr)
            else:
                break
        return arr