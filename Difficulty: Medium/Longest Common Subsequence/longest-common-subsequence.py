class Solution:
    def lcs(self, s1, s2):
        # code here
        # dp = []
        # for i in range(len(s1)):
        #     arr = [-1]*len(s2)
        #     dp.append(arr)
        # def backtrack(ind1,ind2):
        #     if ind1<0 or ind2<0:
        #         return 0
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]
        #     if s1[ind1] == s2[ind2]:
        #         dp[ind1][ind2] = 1 + backtrack(ind1-1,ind2-1)
        #     else:
        #         left = 0 + backtrack(ind1-1,ind2)
        #         right = 0 + backtrack(ind1,ind2-1)
        #         dp[ind1][ind2] = max(left,right)
        #     return dp[ind1][ind2]
        # return backtrack(len(s1)-1,len(s2)-1)
        
        dp = []

        for i in range(len(s1)):
            dp.append([-1] * len(s2))

        dp[0][0] = int(s1[0] == s2[0])

        for i in range(1, len(s2)):
            dp[0][i] = max(dp[0][i-1], int(s1[0] == s2[i]))

        for ind1 in range(1, len(s1)):
            dp[ind1][0] = max(dp[ind1-1][0], int(s1[ind1] == s2[0]))

            for ind2 in range(1, len(s2)):
                if s1[ind1] == s2[ind2]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    left = dp[ind1-1][ind2]
                    right = dp[ind1][ind2-1]
                    dp[ind1][ind2] = max(left, right)

        return dp[-1][-1]
                
                
                
            