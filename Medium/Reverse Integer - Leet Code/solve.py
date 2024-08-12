example1 = 1534236469


def reverse(x: int) -> int:
        strInput = str(x)
        strReversed = ''
        for i in range(len(strInput) -1 , -1, -1):
            if strInput[i] == '-':
                strReversed = '-' + strReversed
            else:
                strReversed += strInput[i]
        
        if int(strReversed) <= -2**31 or int(strReversed) >= 2**31 - 1:
            strReversed = '0'

        return int(strReversed)
    
    
print(reverse(example1))
