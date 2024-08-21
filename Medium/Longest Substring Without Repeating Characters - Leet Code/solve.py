example1 = "dvdf"

def lengthOfLongestSubstring(s: str):
    hmStr = {}
    start = 0
    max_len = 0

    for i in range(len(s)):
        if s[i] in hmStr and hmStr[s[i]] >= start:
            start = hmStr[s[i]] + 1
        hmStr[s[i]] = i
        max_len = max(max_len, i - start + 1)

    return max_len
             
print(lengthOfLongestSubstring(example1))    
