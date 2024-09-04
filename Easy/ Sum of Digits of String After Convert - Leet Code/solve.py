class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for char in s:
            num += str(ord(char) - ord('a') + 1)

        for _ in range(k):
            currentValue = 0
            for n in num:
                currentValue += int(n) 
            num = str(currentValue)
            
        return int(num)
        
