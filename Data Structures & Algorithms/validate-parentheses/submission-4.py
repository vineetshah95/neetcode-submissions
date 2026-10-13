class Solution:
    def isValid(self, s: str) -> bool:
        output = {"}":"{",")":"(","]":"["}
        stack = []
        k = 0
        for i in s:
            if i not in output:
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == output[i]:
                    stack.pop()
                else:
                    return False
            print(stack)
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False
        # k = len(s) - 1
        # k = 0
        # while stack and k < len(s) // 2:
        #     print(output[stack[k]])
        #     if stack.pop() != output[stack[k]]:
        #         return False
        #     k += 1
        # return True