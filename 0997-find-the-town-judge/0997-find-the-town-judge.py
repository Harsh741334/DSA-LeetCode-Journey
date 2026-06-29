class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1 :
            return 1

        if not trust:
            return -1
        judge = {} # A -- TRUST --> B 

        tru = {} #  A  ---> TRUSTED BY --> B

        for u,v in trust:
            if u in judge and v in tru:
                judge[u] = judge[u] + 1
                tru[v] = tru[v] + 1
            elif v in tru:
                tru[v] = tru[v] + 1
                judge[u] = 1
        
            elif u in judge:
                judge[u] = judge[u] + 1
                tru[v] = 1
                        
            else:
                judge[u] = 1
                tru[v]= 1

        size = n-1

        for i in range(1,n+1):
            if i not in judge  and i in tru:
                if tru[i] == size:
                 return i

        return -1
           
           
            
        