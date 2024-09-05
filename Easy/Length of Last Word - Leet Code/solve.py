class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s.split())
        return len(s[len(s) - 1])

  #---------------------------------ANOTHER WAY TO SOLVE-------------------------------------------#

        # strLen = 0
        # i = len(s) - 1
        
        # while i >= 0 and s[i] == ' ':
        #     i -= 1
        
        # while i >= 0 and s[i] != ' ':
        #     strLen += 1
        #     i -= 1
        
        # return strLen
