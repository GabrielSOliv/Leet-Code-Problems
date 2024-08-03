example1 = "abccbaacz"
example2 = "abcdd"

def repeatedCharacter(s: str) -> str:
    letterFrequency = {}
    strTwice = []
    for i in range(len(s)):
        if s[i] in letterFrequency:
            letterFrequency[s[i]] += 1
            if letterFrequency[s[i]] == 2:
                strTwice.append(s[i])
        else:
            letterFrequency[s[i]] = 1

    return strTwice[0]           
            
print(repeatedCharacter(example1))            
            
