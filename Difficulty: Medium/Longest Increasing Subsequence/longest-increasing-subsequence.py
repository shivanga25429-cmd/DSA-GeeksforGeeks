class Solution:
    def lis(self, arr):
        # code here
        def lb(val):
            low = 0
            high = len(ans)
            while low<=high:
                mid = (low+high)//2
                if ans[mid]>=val:
                    high = mid-1
                else:
                    low = mid+1
            return low
                    
                
        ans = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i]<=ans[-1]:
                ind = lb(arr[i])
                ans[ind] = arr[i]
            else:
                ans.append(arr[i])
        return len(ans)
               
