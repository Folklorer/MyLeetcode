# 240725

# 暴力解法
def twoSum(nums: list[int], target: int) -> list[int]:
    for i, x in enumerate(nums): 
        for j in range(i + 1, len(nums)): 
            if x + nums[j] == target:
                return [i, j]

# Hash : 参考 https://leetcode.cn/problems/two-sum/solutions/2326193/dong-hua-cong-liang-shu-zhi-he-zhong-wo-0yvmj/
def twoSum2(nums: list[int], target: int) -> list[int]:
    id = {}
    for idx, x in enumerate(nums):
        if target - x in id:
            return [id[target-x],idx]
        id[x] = idx
    return None
    