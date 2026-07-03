class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            
            #first check starting with first char of starting
            #s[left].isalnum() will check if char is alphanumeric (A-Z) (0-9)
            #but we're negating so it shouldn't be a valid char so we will progress through the str
            while left < right and not s[left].isalnum():
                left += 1

            #second check of the str with the last char occuring at the same time
            while left < right and not s[right].isalnum():
                right -= 1
            
            #lowers each char in str and compares it
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True