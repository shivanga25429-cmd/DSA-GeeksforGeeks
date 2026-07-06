class Solution:
    def DSU(self, n, queries):
        # code here
        parent = []
        for i in range(n+1):
            parent.append(i)
        def find_p(ind):
            if parent[ind] == ind:
                return ind
            parent[ind] = find_p(parent[ind])
            return parent[ind]
        res = []
        for i in queries:
            if i[0] == 1:
                u = find_p(i[1])
                v = find_p(i[2])
                
                if u == v:
                    continue
                
                parent[u] = parent[v]
            else:
                res.append(find_p(i[1]))
        return res
        