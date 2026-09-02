class Solution:
    def cutRod(self, price: list[int]) -> int:
        n = len(price)
        dp = [0] * (n + 1)
    
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp[j] = max(dp[j], price[i - 1] + dp[j - i])
    
        return dp[n]