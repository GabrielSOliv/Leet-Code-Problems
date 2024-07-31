
Example1 = 'aababbab'
Example2 = 'bbaaaaabb'

def minimumDeletions(s: str):
    countB = 0
    Valdeletions = 0

    for i in range(len(s)):
        if s[i] == 'b':
            countB += 1
        elif countB > 0:
            countB -= 1
            Valdeletions += 1

    return Valdeletions       

print('the minimum number of deletions needed to make s balanced in example1 is: ' + str(minimumDeletions(Example1))) 
print('the minimum number of deletions needed to make s balanced in example2 is: ' + str(minimumDeletions(Example2)))                 
