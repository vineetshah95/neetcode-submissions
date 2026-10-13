class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1, hashmap2 = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashmap1[s[i]] = 1 + hashmap1.get(s[i], 1)
            hashmap2[t[i]] = 1 + hashmap2.get(t[i], 1)
        return hashmap1 == hashmap2