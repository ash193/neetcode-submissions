class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            #this calc total sum with first index and last index
            currentSum = numbers[left] + numbers[right]

            #the sum is too big in this instance we need to lower right val ptr
            if currentSum > target:
                right -= 1
            
            #the sum is too small in this instead we need to increase left val ptr
            elif currentSum < target:
                left += 1
            
            else: #this problem numbers are 1-index based instead of 0, so needs to add + 1
                return [left + 1, right + 1]
            

        