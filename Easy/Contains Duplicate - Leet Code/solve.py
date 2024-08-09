example1 = [2,14,18,22,22]


def containsDuplicate(nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i] == nums[i + 1]:
                    return True
            
        return False
        
        
print(containsDuplicate(example1))
