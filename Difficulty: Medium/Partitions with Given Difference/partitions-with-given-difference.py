class Solution:
    def countPartitions(self, arr, diff):
        # code here
        dp = []
        sumi = sum(arr)
        target = sumi-diff
        if target<0 or target%2:
            return 0
        target = target//2
        for i in range(len(arr)):
            new = [0]*(sumi+1)
            dp.append(new)
            dp[i][0] = 1
        if arr[0] == 0:
            dp[0][0] = 2          # empty subset + {0}
        elif arr[0] <= target:
            dp[0][arr[0]] = 1

        for i in range(1,len(arr)):
            for j in range(sumi+1):
                ntake = dp[i-1][j]
                take = 0
                if arr[i]<=j:
                    take = dp[i-1][j-arr[i]]
                dp[i][j] = ntake + take
        return dp[len(arr)-1][target]
