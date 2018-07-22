class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = A*2 - 1
        result = [[[]for x in range(size)] for y in range(size)]
        top=0
        left=0
        right=size-1
        bottom=size-1
        while top <= bottom and left <= right:
            for i in range(top, bottom+1):
                result[i][left] = A
                result[i][right] = A
            for i in range(left, right+1):
                result[top][i] = A
                result[bottom][i] = A
            top += 1
            left += 1
            right -= 1
            bottom -= 1
            A -= 1
        return result
