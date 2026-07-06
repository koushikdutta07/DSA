class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = dict()
        for i in range(len(nums)):
            if target-nums[i] in ref:
                return [i,ref.get(target-nums[i])]
            ref[nums[i]]=i         
        return [-1,-1]

        