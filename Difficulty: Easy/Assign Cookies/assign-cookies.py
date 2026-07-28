class Solution:
    def maxChildren(self, g, s):
        #code here
        i=0
        j=0
        c=0
        g.sort()
        s.sort()
        l1=len(g)
        l2=len(s)
        while i<l1 and j<l2:
            if s[j]>=g[i]:
                c+=1
                i+=1
            j+=1
        return c
