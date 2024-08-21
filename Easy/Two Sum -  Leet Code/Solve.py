
example1 = [2,7,11,15]
example2 = [3,2,4]
example3 = [3,3]

target1 = 9
target2 = 6
target3 = 6


def twoSum(target:int, nums:list) ->list:
    hashMap = {}
    for idx, i in enumerate(nums):
        if hashMap.get(i) is not None:
            return [hashMap.get(i), idx]
        hashMap[target - i] = idx 
            
print (str(twoSum(target1, example1)) + " are the two numbers necessary to reach the target value: " + str(target1) + ".")
print (str(twoSum(target2, example2)) + " are the two numbers necessary to reach the target value: " + str(target2) + ".")
print (str(twoSum(target3, example3)) + " are the two numbers necessary to reach the target value: " + str(target3) + ".")
