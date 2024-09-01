class Solution:
    def reverseStr(self, s: list) -> list:
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        
        return s

    def finalString(self, s: str) -> str:
        s = list(s)
        newStr = []
        
        for i in range(len(s)):
            if s[i] == 'i':
                newStr = self.reverseStr(newStr)
            else:
                newStr.append(s[i])

        return str(''.join(newStr))
