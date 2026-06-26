class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = str(x)
        if num == num[::-1]:
            return True
        else: 
            return False
        