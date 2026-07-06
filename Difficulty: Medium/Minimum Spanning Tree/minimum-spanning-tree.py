class Solution:
    def spanningTree(self, V, edges):
        import heapq
        pq = []
        heapq.heappush(pq,[0,0])
        vis = [0]*V
        adj = []
        for _ in range(V):
            adj.append([])
        for src,dst,w in edges:
            adj[src].append([w,dst])
            adj[dst].append([w,src])
        sumi = 0
        while pq:
            w,curr = heapq.heappop(pq)
            if vis[curr]:
                continue
            sumi += w
            vis[curr] = 1
            for i in adj[curr]:
                if vis[i[1]]:
                    continue
                heapq.heappush(pq,[i[0],i[1]])
        return sumi