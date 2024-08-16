example1 = 'yrpjofyzubfsiypfre'

def longestContinuousSubstring(s: str) -> int:
        count = 1
        currentCount = 1
    
        for i in range(1, len(s)):
            
            if ord(s[i]) == ord(s[i - 1]) + 1:
                currentCount += 1
                count = max(count, currentCount)
            else:
                currentCount = 1
    
        return count

print(longestContinuousSubstring(example1))
