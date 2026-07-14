class Solution:
    def minCost(self, height):
        # code here
        prev2 = None
        prev = 0
        for ind in range(1,len(height)):
            left = prev + abs(height[ind]-height[ind-1])
            right = float("inf")
            if ind > 1:
                right = prev2 + abs(height[ind]-height[ind-2])
            prev2 = prev
            prev = min(left,right)
        return prev
            
        