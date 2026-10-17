class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        string = ""
        maxLen = 0
        for l in range(len(s)):
            while r < len(s) and s[r] not in string:
                string += s[r]
                r += 1
            maxLen = max(len(string), maxLen)
            string = s[l+1:r]
        return maxLen
            


