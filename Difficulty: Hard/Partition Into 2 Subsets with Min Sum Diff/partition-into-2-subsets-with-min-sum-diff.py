class Solution:
    def minDifference(self, arr):
        sumi = sum(arr)
        n = sumi + 1

        dp = [False] * n
        dp[0] = True

        for num in arr:
            for j in range(sumi, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        mini = float("inf")
        for j in range(sumi // 2 + 1):
            if dp[j]:
                mini = min(mini, sumi - 2 * j)

        return mini