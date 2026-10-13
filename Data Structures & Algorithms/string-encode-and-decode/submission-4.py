class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + str(len(i)) + "#" + i
        return string

    def decode(self, s: str) -> List[str]:
        lst = []
        strs = ""
        j = len(s)
        i = 0
        while i < j:
            k = i
            while s[k] != "#":
                k += 1
            length = int(s[i:k])
            lst.append(s[k+1:k+1+length])
            i = k + 1 + length
        return lst