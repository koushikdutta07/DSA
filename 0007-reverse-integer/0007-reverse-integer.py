class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False 
        if x<0:
            x=-x
            isNeg = True
        s = str(x)
        ans = -int(s[::-1]) if isNeg else int(s[::-1]) 
        return 0 if ans < -2**31 or ans > 2**31-1 else ans
        