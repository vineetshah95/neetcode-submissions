class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        maxCount = 0
        for i in hashset:
            if i - 1 not in hashset:
                count = 1
                current = i
                while current + 1 in hashset:
                    count += 1
                    current += 1
                maxCount = max(maxCount, count)
        return maxCount