class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. target_num > index => pass
        result = []
        for i, num in enumerate(nums):
            for compare in nums[i + 1 :]:
                if num + compare == target:
                    result.append(i)
                    result.append(nums.index(compare, nums.index(num) + 1))
                    break
        return result
