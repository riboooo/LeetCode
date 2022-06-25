class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        inner = 0
        for pointer in range(len(nums)):
            if nums[pointer] == 1:
                inner += 1
                if inner > max:
                    max = inner
            else:
                inner = 0
        return max