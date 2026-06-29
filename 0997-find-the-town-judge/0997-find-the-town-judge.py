class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_count = [0 for i in range(n)]
        for u,v in trust:
            trust_count[u -1]-=1 # <--- in degree
            trust_count[v -1]+=1  #<--- out degree
        for i in range(n):
            if trust_count[i]==(n-1):
                return i+1
        return -1