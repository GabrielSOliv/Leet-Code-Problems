def repeatedCharacter(s: str) -> str:
    hm = {}

    for i in  range(len(s)):
        hm[s[i]] = 1 + hm.get(s[i], 0)
        if hm[s[i]] == 2:
            return s[i]    
