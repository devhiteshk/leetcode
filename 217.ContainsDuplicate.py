class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Method 1
        D = {}
        for i in nums:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        for keys in D:
            if D[keys] >=2:
                return True
        return False
        
        # method 2
        X = collections.Counter(nums)
        # print(X)
        for i in X:
            if X[i]>=2:
                return True
        return False