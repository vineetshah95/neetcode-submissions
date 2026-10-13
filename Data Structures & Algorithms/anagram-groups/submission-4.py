class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            k = sorted(i)
            if tuple(k) not in hashmap:
                hashmap[tuple(k)] = [i]
            else:
                hashmap[tuple(k)].append(i)
        # print(hashmap)
        lst = []
        for i in hashmap.values():
            lst.append(i)

        return lst