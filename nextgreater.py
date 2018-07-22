class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        result = [-1 for i in range(len(A))]
        for i in range(len(A) - 1):
            current = A[i]
            nextGreaterIndex = i + 1
            while A[nextGreaterIndex] <= current and nextGreaterIndex < len(A) - 1:
                nextGreaterIndex += 1
            if nextGreaterIndex == len(A) - 1 and A[nextGreaterIndex] <= current:
                result[i] = -1
            else:
                result[i] = A[nextGreaterIndex]
        return result
