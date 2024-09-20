class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = []
        space_set = set(spaces)
    
        for i in range(len(s)):
            if i in space_set:
                out.append(' ')
            out.append(s[i])
        
        return ''.join(out)
