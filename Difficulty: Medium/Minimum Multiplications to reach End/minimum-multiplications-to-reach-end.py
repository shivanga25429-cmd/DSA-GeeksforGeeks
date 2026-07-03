class Solution:
    def minSteps(self, arr, start, end):
        # code here
        if start == end:
            return 0
            
        import heapq
        pq= []
        heapq.heappush(pq,[0,start])
        dis = [float("inf")]*1000
        dis[start] = 0
        while pq:
            step,val = heapq.heappop(pq)
            if step>dis[val]:
                continue
            if val == end:
                return step
            for i in arr:
                newval = (val*i)%1000
                if step+1<dis[newval]:
                    dis[newval] = step + 1
                    heapq.heappush(pq,[step+1,newval])
        if dis[end] == float("inf"):
            return -1
        return dis[end]
                
                
