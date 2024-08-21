example1 = [2,14,18,22,22]


def containsDuplicate(nums: list[int]) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                return True
            else:
                hm[nums[i]] = 1
        
        
print(containsDuplicate(example1))
