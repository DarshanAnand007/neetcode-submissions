class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        for num in nums:
            if num == 1:
                counter += 1
                if counter > result:
                    result = counter
            else:
                counter = 0
        return result