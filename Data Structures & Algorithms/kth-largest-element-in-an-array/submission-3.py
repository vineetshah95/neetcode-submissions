class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[-n for n in nums]
        heapq.heapify(max_heap)
        print(max_heap)
        j = 0
        while j < k - 1:
            heapq.heappop(max_heap)
            j += 1
        return -1 * max_heap[0]