class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = set()
        for i in range(len(nums)):
            if nums[i] in mySet:
                nums[i]=200
            else:
                mySet.add(nums[i])
        nums = nums.sort()
        return len(mySet)
        