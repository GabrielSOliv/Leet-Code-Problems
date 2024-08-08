example1 = 122182 #FXSH


def convertToTitle(columnNumber: int) -> str:
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    letterArray = []
    letterStr = ''
    divisionfloat = 0
    
    columnNumber = columnNumber - 1
    while (columnNumber >= 0):
        divisionfloat = columnNumber % 26
        letterArray.append(divisionfloat + 1)
        columnNumber = (columnNumber // 26) - 1
        
    letterArray.reverse()
    
    for i in letterArray:
        letterStr += letters[i - 1]
    
    return letterStr    

print(convertToTitle(example1))
