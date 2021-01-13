def robber(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    print(dp)
    return dp[n-1]


nums = [8, 4, 1, 9, 3, 7, 2]
robber(nums)