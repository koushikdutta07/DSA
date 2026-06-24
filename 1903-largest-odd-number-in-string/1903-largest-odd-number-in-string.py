class Solution:
    def largestOddNumber(self, num: str) -> str:
        index = len(num)
        for i in num[::-1]:
            if int(i)%2==0:
                index-=1
            else:
                break
        return num[:index]
