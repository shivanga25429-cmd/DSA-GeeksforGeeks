class Solution:
    def knapSack(self, val, wt, capacity):
        dp = []
    
        for i in val:
            arr = [0] * (capacity + 1)
            dp.append(arr)
    
        for i in range(capacity + 1):
            dp[0][i] = val[0] * (i // wt[0])
        
        for ind in range(1,len(val)):
            for weight in range(capacity+1):
                ntake = dp[ind - 1][ weight]
                take = float("-inf")
                if wt[ind] <= weight:
                    take = val[ind] + dp[ind][ weight - wt[ind]]
    
                dp[ind][weight] = max(ntake, take)
                
        return dp[-1][capacity]
        def backtrack(ind, weight):
            if ind == 0:
                return dp[0][weight]
    
            if dp[ind][weight] != -1:
                return dp[ind][weight]
    
            ntake = backtrack(ind - 1, weight)
    
            take = float("-inf")
            if wt[ind] <= weight:
                take = backtrack(ind, weight - wt[ind])
    
            dp[ind][weight] = max(ntake, take)
            return dp[ind][weight]
    
        backtrack(len(val) - 1, capacity)
        return dp[-1][capacity]