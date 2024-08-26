example1 = 121
example2 = -121
example3 = 10 

def isPalindrome(x: int) -> bool:
    numStr = str(x)
    leftP, rightP = 0, len(numStr) - 1
    
    while leftP < rightP:
        if numStr[leftP] != numStr[rightP]:
            return False
        
        leftP, rightP = leftP + 1, rightP - 1

    return True
      

print("the result for the example1 is: " + str(isPalindrome(example1)) + " because is a palindrome")
print("the result for the example2 is: " + str(isPalindrome(example2)) + " because isn't a palindrome")
print("the result for the example3 is: " + str(isPalindrome(example3)) + " because isn't a palindrome")
