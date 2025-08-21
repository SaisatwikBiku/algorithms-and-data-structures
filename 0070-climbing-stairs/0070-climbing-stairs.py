class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Bottom up tabulation

        #creating table to store the results
        dp = [0] * (n+1)

        # base cases:
        dp[1], dp[2] = 1,2

        # formulating recurrence relation
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]