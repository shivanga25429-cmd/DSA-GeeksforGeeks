class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        arr = [False]*(leaves+1)
        frogs = set(frogs)
        for strength in frogs:
            pos = strength
            while pos<=leaves:
                arr[pos] = True
                pos += strength
        count = 0
        for i in arr:
            if not i:
                count += 1
        return count-1
            
            