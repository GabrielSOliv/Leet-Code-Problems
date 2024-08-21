ex = [1, 1, 2, 2, 3]

def singleNumber(nums: list[int]) -> int:
	hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1

        return min(hashMap, key=hashMap.get)

print(singleNumber(ex))
