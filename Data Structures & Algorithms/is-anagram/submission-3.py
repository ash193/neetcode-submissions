class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #this will compare the count of letters against each str
        return self.count(s) == self.count(t)
    
    def count(self, str1):
        #this new function keeps track of the appearances of each char
        totalCount = {}

        for char in str1:
            if char not in totalCount:
                totalCount[char] = 0
            totalCount[char] += 1
        
        return totalCount

        