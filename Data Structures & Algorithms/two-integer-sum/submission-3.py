class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in hashmap:
                return [hashmap[nums[i]],i]
            if diff not in hashmap:
                hashmap[diff] = i
            # else:
            #     hashmap[diff].append(i)