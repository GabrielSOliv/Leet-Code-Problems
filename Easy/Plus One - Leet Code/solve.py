example1 = [9,8,7,6,5,4,3,2,1,0]

def plusOne(digits: list[int]) -> list[int]:
        digitStr = ''
        for i in range(len(digits)):
            digitStr += str(digits[i])
            
        digitSumed = str(int(digitStr) + 1) 
        
        result = []
        for i in range(len(digitSumed)):
            result.append(int(digitSumed[i]))
        
        return result
