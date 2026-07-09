from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        parent = list(range(rows*cols))
        visited = [False]*(rows*cols)
        def find(node):
            if node!=parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        count = 0
        arr = []
        for i in operators:
            u = cols*i[0]+i[1]
            if visited[u]:
                arr.append(count)
                continue
            count += 1
            visited[u] = True
            if i[0]>0 and visited[u-cols]:
                if find(u)!=find(u-cols):
                    count-=1
                    parent[find(u)] = find(u-cols)
            if i[1]>0 and visited[u-1]:
                if find(u)!=find(u-1):
                    count-=1
                    parent[find(u)] = find(u-1)
            if i[0]<rows-1 and visited[u+cols]:
                if find(u)!=find(u+cols):
                    count-=1
                    parent[find(u)] = find(u+cols)
            if i[1]<cols-1 and visited[u+1]:
                if find(u)!=find(u+1):
                    count-=1
                    parent[find(u)] = find(u+1)
            arr.append(count)
        return arr
                
                
            
            