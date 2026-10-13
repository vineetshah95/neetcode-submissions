class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            val = tuple(sorted(i))
            if val not in hashmap:
                hashmap[val] = [i]
            else:
                hashmap[val].append(i)
        lst = []
        for i in hashmap:
            lst.append(hashmap[i])
        return lst