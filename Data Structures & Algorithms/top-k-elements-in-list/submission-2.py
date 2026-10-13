from sortedcontainers import SortedDict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] = hashmap[i] + 1
        # print(hashmap)
        heap = []
        for i in hashmap:
            heapq.heappush(heap, (hashmap[i],i))
            if len(heap) > k:
                heapq.heappop(heap)
        lst = []
        for i in range(k):
            lst.append(heapq.heappop(heap)[1])
        return lst
        # lst = []
        # print(hashmap)
        # for i in hashmap:
        #     if k > 0:
        #         lst.append(i)
        #         k -= 1
        # return lst