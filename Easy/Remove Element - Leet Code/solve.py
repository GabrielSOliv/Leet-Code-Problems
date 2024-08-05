example1 = [3,2,2,3]
val1 = 3

def removeElement(nums: list[int], val: int) -> int:
    newArray = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[newArray] = nums[i]
            newArray += 1
    return newArray

print(removeElement(example1, val1))
