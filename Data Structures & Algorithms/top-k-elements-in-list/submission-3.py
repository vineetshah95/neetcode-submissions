class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            freq[value].append(key)
        lst = []
        for i in range(len(freq)-1,0, -1): #indexes
            for n in freq[i]:
                if k > 0:
                    lst.append(n)
                k -= 1
                if k < 0:
                    return lst
        return lst
