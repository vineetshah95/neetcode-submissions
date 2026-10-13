class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        maxLen = 0
        res = ""
        for l in range(len(s)):
            while r <= len(s) - 1 and s[r] not in res:
                res += s[r]
                r += 1
                print(res)
                maxLen = max(maxLen, len(res))
            res = res[1:]
        return maxLen