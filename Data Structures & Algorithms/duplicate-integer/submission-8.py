class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for first in range(len(nums)):
            if nums[first] in seen:
                return True
            seen.add(nums[first])
        return False