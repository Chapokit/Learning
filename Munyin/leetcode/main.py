class Solution(object):
    def isPalindrome(self, x):
        # Early return for negative numbers and numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Check if the original number is equal to the reversed half
        return x == reversed_half or x == reversed_half // 10