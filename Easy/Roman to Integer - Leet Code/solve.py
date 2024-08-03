Example1 = 'MCMXCVI'

roman_symbols = [['I', 1],['IV', 4],['V', 5],['IX', 9],['X', 10],['XL', 40],['L', 50],['XC', 90],['C', 100],['CD', 400],['D', 500],['CM', 900],['M', 1000]]

def romanToInt(s: str) -> int:
    strSum = 0
    next = False
    found = False
    
    for j in range(len(s)):
        if next == True: 
            next = False 
            continue
        
        found = False
        
        if (s[j] == 'I' or s[j] == 'X' or s[j] == 'C') and (j + 1 < len(s)):
           for i in range(len(roman_symbols)):
                if roman_symbols[i][0] == s[j]+s[j+1]:
                    strSum += roman_symbols[i][1]
                    next = True
                    found = True
        if not found:
            for i in range(len(roman_symbols)):
                if roman_symbols[i][0] == s[j]:
                    strSum += roman_symbols[i][1]
                    next = False
                    found = False
                
    return strSum


print(romanToInt(Example1))
