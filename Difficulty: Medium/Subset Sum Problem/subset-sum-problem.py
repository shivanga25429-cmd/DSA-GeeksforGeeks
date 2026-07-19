class Solution:
    def isSubsetSum(self, arr, sum):
        m = len(arr)
        n = sum + 1

        dp = []
        for i in range(m):
            arr2 = [False] * n
            dp.append(arr2)

        for i in range(m):
            dp[i][0] = True

        if arr[0] <= sum:
            dp[0][arr[0]] = True

        for i in range(1, m):
            for j in range(1, n):
                not_take = dp[i - 1][j]
                take = False
                if j >= arr[i]:
                    take = dp[i - 1][j - arr[i]]
                dp[i][j] = take or not_take

        return dp[m - 1][sum]