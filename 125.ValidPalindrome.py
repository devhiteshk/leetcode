class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Best Approach
        # final_string = re.sub('[^A-Za-z0-9]+', '', s).lower()
        # reverse=final_string[::-1]
        # if(final_string==reverse):
        #     return True
        # else:
        #     return False
        
        
        x = ""
        for i in range(len(s)):
            if s[i].isalnum():
                x += s[i].lower()
                
        
        if x == x[::-1]:
            return True
        return False