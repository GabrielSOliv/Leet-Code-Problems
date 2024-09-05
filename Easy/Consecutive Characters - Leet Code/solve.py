class Solution:
    def maxPower(self, s: str) -> int:
        letterCount = 0
        CurrentCount = 1

        for i in range(len(s)):
            if (i + 1) < len(s) and s[i] == s[i + 1]:
                CurrentCount += 1
            else:
                letterCount = max(letterCount, CurrentCount)
                CurrentCount = 1

        return letterCount
