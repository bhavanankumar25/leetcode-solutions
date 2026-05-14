class Solution:
    def isPalindrome(self, x):
        s =str(x)
        if s == s[::-1]:
             return True 
        else:
            return False 
        
"""
convert the number to a string, 
then check if it reads the same forwards and backwards.
"""