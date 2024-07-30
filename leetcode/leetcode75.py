# 240730

def sortColors(nums: list[int]) -> None:
    zero = nums.count(0)
    one = nums.count(1)
    for i in range(len(nums)):
        if i < zero:
            nums[i] = 0
        elif zero <= i and i < zero+one:
            nums[i] = 1
        else:
            nums[i] = 2
    print(nums)

nums = [0,2,2,2,2]
sortColors(nums)