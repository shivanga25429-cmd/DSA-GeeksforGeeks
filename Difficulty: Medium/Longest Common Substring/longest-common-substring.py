class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        dp = []
        rows = len(s1)+1
        cols = len(s2)+1
        for i in range(rows):
            arr = [0]*(cols)
            dp.append(arr)
        maxi = 0
        for i in range(1,rows):
            for j in range(1,cols):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                maxi = max(maxi,dp[i][j])
        return maxi