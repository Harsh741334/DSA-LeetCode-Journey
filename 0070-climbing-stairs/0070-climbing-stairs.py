class Solution:
    def climbStairs(self, n: int) -> int:
        nums = []

        nums.append(1)
        nums.append(2)

        for i in range(2,n):
           total = nums[i-1] + nums[i-2]
           nums.append(total)
        return nums[n-1]

      

            

        

       
        