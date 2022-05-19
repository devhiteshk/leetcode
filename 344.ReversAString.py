class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Method 1
        
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        
        #Method 2
        s[:] = s[::-1]