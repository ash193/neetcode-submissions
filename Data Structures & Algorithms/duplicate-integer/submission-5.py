class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using a set to keep track of numbers
        #set allows for no duplicates
        numsList = set()

        for num in nums:

            #this will check if the number already exists in the set
            if num in numsList:
                return True
            numsList.add(num)
            #we want to add the number to the set if it's first appearance
        
        return False


        