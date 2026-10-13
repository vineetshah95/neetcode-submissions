class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for p in points:
            dist = math.sqrt((p[0] - 0) ** 2 + (p[1] - 0) ** 2)
            heap.append([dist, p])
        heapq.heapify(heap)
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans