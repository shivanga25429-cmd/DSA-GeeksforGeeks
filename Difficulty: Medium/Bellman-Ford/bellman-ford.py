class Solution:
    def bellmanFord(self, v, edges, src):
        #code here
        dis = [float("inf")]*v
        dis[src] = 0
        for _ in range(v-1):
            for curr,dst,weight in edges:
                if dis[curr] + weight<dis[dst]:
                    dis[dst] = dis[curr] + weight
        for curr,dst,weight in edges:
            if dis[curr] + weight<dis[dst]:
                return [-1]
        for i in range(v):
            if dis[i] == float("inf"):
                dis[i] = 100000000
            
        return dis
                
            
        