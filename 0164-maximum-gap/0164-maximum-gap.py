class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <2:
            return 0
        num = sorted(nums)
        maxx = -1

        for i in range(1,len(num)):
            temp = abs(num[i-1] - num[i])
            maxx = max(maxx,temp)

        return maxx


        
        