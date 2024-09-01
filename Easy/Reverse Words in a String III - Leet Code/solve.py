class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        newStr = []
        for word in s:
            
            left, right = 0, len(word) -1
            word = list(word)
            
            while left < right:
                word[left], word[right] = word[right], word[left]
                left, right = left + 1, right - 1
            
            newStr.append(str(''.join(word)))
        
        return(str(' '.join(newStr)))
