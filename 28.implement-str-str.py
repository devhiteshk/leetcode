#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H = len(haystack)
        N = len(needle)
        if N == 0 or H == 0:
            return 0
        else:
            for i in range(0, H - N + 1):
                if haystack[i:i+N] == needle:
                    return i
        return -1
        
# @lc code=end

