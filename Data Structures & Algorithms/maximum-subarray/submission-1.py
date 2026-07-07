class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]

        for i in range(0, len(nums)):
            #we don't want negative values so we reset
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[i] #if positive we add it to curr sum

            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum
        