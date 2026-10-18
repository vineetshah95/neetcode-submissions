class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a hashmap and iterate through the input s
        # key should be the character you chose to replace
        # as you traverse through the string (update the pointers)
        # and add or subtract the replacements as the value of k allows 
        left, right = 0, 0
        hashmap = {}
        maxLen = 0
        string = ""
        while right < len(s):
            string += s[right]
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            if (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left = left + 1
            maxLen = max(maxLen, right-left+1)
            right += 1
        return maxLen
            
            
            
