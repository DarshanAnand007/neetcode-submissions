class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distint = set(nums)
        if len(distint) != len(nums):
            return True
        return False