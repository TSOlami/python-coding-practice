class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pDict = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in pDict:
                if stack and stack[-1] == pDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return False if stack else True
