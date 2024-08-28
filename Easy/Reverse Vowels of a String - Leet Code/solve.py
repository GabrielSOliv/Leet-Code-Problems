class Solution:
    def isValid(self, c: str) -> bool:
        return c.lower() in 'aeiou'
    
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s_list = list(s)

        while left < right:
            if not self.isValid(s_list[left]):
                left += 1
            elif not self.isValid(s_list[right]):
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left, right = left + 1, right - 1
        
        return ''.join(s_list)
