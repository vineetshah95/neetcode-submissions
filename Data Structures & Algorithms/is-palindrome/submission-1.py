class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0, len(s) - 1
        s = s.lower()
        s = s.strip()
        print(s)
        while i < j:
            # if s[i]!= s[j] and (s[i] or s[j] not in '[A-Za-z0-9]'):
            #     return False
            if not re.match(r'[A-Za-z0-9]', s[i]):
                i += 1
            elif not re.match(r'[A-Za-z0-9]', s[j]):
                j-=1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j-= 1
        return True