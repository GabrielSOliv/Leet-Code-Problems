class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        listOut = []
        for i in range(len(nums)):
            hm[nums[i]] = 1 + hm.get(nums[i], 0)
            if hm[nums[i]] > (len(nums) // 3):
                if not nums[i] in listOut:
                    listOut.append(nums[i])
        
        return listOut
