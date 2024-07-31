Example1 = [3,2,3]
Example2 = [2,2,1,1,1,2,2]

import statistics
def majorityElement(nums:list[int]):
    mode_value = statistics.mode(nums)
    return mode_value
       
##______________________________________________________________Harded coded version_______________________________________________________________________________________________

def majorityElement2(nums:list[int]):
    nums.sort()
    nums_length = len(nums)
    mid_value = nums_length // 2
    mode = nums[mid_value]
    return mode
