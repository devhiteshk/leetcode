class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0]>=nums[-1]:
            for i in range(len(nums)-1):
                if nums[i+1]>nums[i]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i+1]<nums[i]:
                    return False
        return True