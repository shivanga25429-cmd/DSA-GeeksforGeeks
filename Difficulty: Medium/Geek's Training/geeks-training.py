class Solution:
    def maximumPoints(self, mat):
        # code here
        dp = [max(mat[0][1],mat[0][2]),max(mat[0][0],mat[0][2]), max(mat[0][0],mat[0][1]),max(mat[0])]
        for day in range(1,len(mat)):
            dummy = [0]*4
            for last in range(4):
                for task in range(3):
                    if last!=task:
                        dummy[last] = max(dummy[last], mat[day][task] + dp[task])
            dp = dummy[::]
        return dp[3]
    
            
        
        