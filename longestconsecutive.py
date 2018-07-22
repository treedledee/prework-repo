class Solution:

    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hashset = {}
        for i in range(len(A)):
            hashset[A[i]] = 1
        longest = 0
        for element in hashset:
            count = 0
            if (element - 1) not in hashset:
                count = 1
                greater = element + 1
                while greater in hashset:
                    greater += 1
                    count += 1
            longest = max(count, longest)
        return longest
