class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm = {}
        listOut = []
        for i in range(len(nums)):
            hm[nums[i]] = 1 + hm.get(nums[i], 0)
            if hm[nums[i]] >= 2:
                listOut.append(nums[i])
        
        return listOut
