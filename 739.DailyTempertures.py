class Solution:
    def dailyTemperatures(self, temp):
        
        # BRUTE FORCE METHOD
        
#         ans = []
#         i = 0
#         j = 0
#         count = 0
#         while i< len(temp)-1:
#             if temp[i] < temp[j]:
#                 ans.append(count)
#                 i += 1
#                 j = i
#                 count = 0
                
#             else:
#                 j += 1
#                 if j == len(temp):
#                     ans.append(0)
#                     count = 0
#                     i += 1
#                     j = i
#                 else:
#                     count+=1
                    
#         return(ans + [0])



        # STACK BASED APPROACH
    
        # n = len(temperatures)
        # if n==1:
        #     return [0]
        # ans = [0]*n
        # max_ = temperatures[-1]
        # for i in range(n-2,-1,-1):
        #     val = temperatures[i]
        #     if val>=max_:
        #         max_ = val
        #         continue
        #     else:
        #         nday = 1
        #         while temperatures[i+nday]<=val:
        #             nday += ans[i+nday]
        #         ans[i] = nday
        # return ans


        # OPTIMAL METHOD T.C. O(N)
        
        n = len(temp)
        hottest = 0
        answer = [0] * n
        
        for i in range(n - 1, -1, -1):
            current_temp = temp[i]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temp[i + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[i + days]
            answer[i] = days

        return answer