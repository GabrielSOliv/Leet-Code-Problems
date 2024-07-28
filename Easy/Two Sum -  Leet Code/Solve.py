
example1 = [2,7,11,15]
example2 = [3,2,4]
example3 = [3,3]

target1 = 9
target2 = 6
target3 = 6


def twoSum(target:int, nums:list) ->list:
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
print (str(twoSum(target1, example1)) + " are the two numbers necessary to reach the target value: " + str(target1) + ".")
print (str(twoSum(target2, example2)) + " are the two numbers necessary to reach the target value: " + str(target2) + ".")
print (str(twoSum(target3, example3)) + " are the two numbers necessary to reach the target value: " + str(target3) + ".")
