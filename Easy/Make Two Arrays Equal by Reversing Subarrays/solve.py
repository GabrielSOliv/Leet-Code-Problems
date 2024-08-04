example1 = [2,4,1,3]
target1 = [1,2,3,4]

def canBeEqual(target: list[int], arr: list[int]) -> bool:
    arr.sort()
    target.sort()
    if arr == target:
            return True
    else: return False      
        
print(canBeEqual(target1,example1)) 
