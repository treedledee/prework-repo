import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        capacity = B
        heap = []
        for index in range(len(A)):
            if len(heap) < capacity:
                heapq.heappush(heap, -A[index])
            else:
                heapq.heapreplace(heap, -A[index])
        return (-heap[0])
