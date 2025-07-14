N = int(input())

# dp
dp = [0] * 1000001 # 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N

# bottom up 
for i in range(2, N+1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 : 
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i % 3 == 0 : 
        dp [i] = min(dp[i], dp[i//3] + 1)
    


print(dp[N])