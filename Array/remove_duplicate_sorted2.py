A = [1,1,1,2,2,3]

def removeDuplicateA(nums):
    n = len(nums)
    if nums is None:
        return 0
    if n < 3:
        return n
    j = 2
    for i in range(2, len(nums)):
        if nums[i] == nums[j-2]:
            continue
        else:
            nums[j] = nums[i]
            j += 1
    print(f"New array: {nums}")

def removeDuplicateB(nums):
    n = len(nums)
    if nums is None:
        return 0
    if n < 3:
        return n
    j = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1
    print(f"New array: {nums}")

def removeDuplicateC(nums):
    if nums is None:
        return 0
    n = len(nums)
    if n < 3:
        return n
    i, j = 0,2

    while (j < n):
        if nums[j] == nums[i] and nums[j] == nums[i-1]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1
    print(f"New array: {nums}")

removeDuplicateC(A)
        

