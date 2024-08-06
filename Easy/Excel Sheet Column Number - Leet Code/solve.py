example1 = 'AB'


def titleToNumber(columnTitle: str) -> int:
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    countLetter = 0
    letterPosition = 0
    exponent = 0
    for i in range(len(columnTitle)):
        for k in range(len(letters)):
            if columnTitle[i] == letters[k]:
                letterPosition = k + 1
                exponent = (len(columnTitle)) - (i + 1)
                countLetter += letterPosition * 26**exponent
    
    return countLetter


print(titleToNumber(example1))
