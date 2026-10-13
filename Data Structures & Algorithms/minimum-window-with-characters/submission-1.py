from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        countT = Counter(t)
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        i = 0
        for j in range(len(s)):
            window[s[j]] = 1 + window.get(s[j], 0)
            if s[j] in countT and window[s[j]] == countT[s[j]]:
                have += 1
            while have == need:
                if (j - i + 1) < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                window[s[i]] -= 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                i += 1
        l, r = res
        return "" if resLen == float("infinity") else s[l:r+1]