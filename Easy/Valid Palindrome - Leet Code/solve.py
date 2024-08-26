class Solution:
    def isValid(self, s: str) -> bool:
        if (ord('A') <= ord(s) <= ord('Z') or
           ord('a') <= ord(s) <= ord('z') or
           ord('0') <= ord(s) <= ord('9')):
           return True
        
        return False
    

    def isPalindrome(self, s: str) -> bool:
        lPointer, rPointer = 0, len(s) - 1

        while lPointer < rPointer:
            while lPointer < rPointer and not self.isValid(s[lPointer]):
                lPointer += 1
            
            while lPointer < rPointer and not self.isValid(s[rPointer]):
                rPointer -= 1
            
            if lPointer < rPointer:
                if s[lPointer].lower() != s[rPointer].lower():
                    return False
                
            lPointer += 1
            rPointer -= 1

        return True

    
