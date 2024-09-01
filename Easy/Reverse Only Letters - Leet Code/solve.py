class Solution:
    def isValid(self, c: str) -> bool:
        c = c.lower()
        return ord('a') <= ord(c) <= ord('z')

    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            if not self.isValid(s[left]):
                left += 1
            elif not self.isValid(s[right]):
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
            
        return str(''.join(s))
