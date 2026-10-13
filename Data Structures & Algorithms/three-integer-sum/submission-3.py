class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            l = i + 1
            j = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < j:

                
                if nums[i] + nums[l] + nums[j] > 0:
                    j -= 1
                
                elif nums[i] + nums[l] + nums[j] < 0:
                    l += 1
                
                else:
                    # if nums[i] + nums[l] + nums[j] == 0:
                        res.append([nums[i], nums[l], nums[j]])
                        l += 1
                        j -= 1
                        while nums[l] == nums[l-1] and l < j:
                            l += 1
        return res