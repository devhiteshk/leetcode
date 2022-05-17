def Reverse(arr, start, end):
    while start<end:
        arr[start], arr[end] = arr[end],  arr[start]
        start += 1
        end -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return nums
        # if len(nums) == 2:
        #     if k%2 == 0:
        #         return nums
        #     else:
        #         nums[0], nums[1] = nums[1], nums[0]
        #         return nums
        # if k>len(nums):
        #     while k>0:             # Brute Force Method T.C. O(n^2) S.C. O(1)
        #         temp = nums[-1]
        #         for i in reversed(range(len(nums))):
        #             nums[i] = nums[i-1]
        #         nums[0] = temp
        #         k -= 1
        
        else:
            k = k%len(nums)          # Second Method O(1) S.C. and O(n) T.C.
            Reverse(nums, 0, len(nums)-1)
            Reverse(nums, 0, k-1)
            Reverse(nums, k, len(nums)-1)
        
        # Third Method O(n) S.C.
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]