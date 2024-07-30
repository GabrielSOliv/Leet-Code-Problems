example1 = 121
example2 = -121
example3 = 10 

def isPalindrome(x: int) -> bool:
    str_num = str(x)
    str_reorganized = ""
    for i in range(len(str_num) - 1,-1, -1):
        str_reorganized += str_num[i]
    if str_num == str_reorganized:
        return True
    else:
        return False
      

print("the result for the example1 is: " + str(isPalindrome(example1)) + " because is a palindrome")
print("the result for the example1 is: " + str(isPalindrome(example2)) + " because isn't a palindrome")
print("the result for the example1 is: " + str(isPalindrome(example3)) + " because isn't a palindrome")
