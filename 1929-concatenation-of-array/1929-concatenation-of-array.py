class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = list()
        for i in range(len(nums)):
            res.append(nums[i])
        for i in range(len(nums)):
            res.append(nums[i])
        return res
        