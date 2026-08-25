amt = 10
coins = [1,2,5,10]

dp =  [len(coins)][amt+1]

for i in range(len(coins)):
    for j in range(amt+1):

        if dp [0][j] % j == 0:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

        if dp[i][0] > j:
            dp [i][0] = dp[i-1][0]

        dp [i][j] = dp[i][j-i]

print(dp[-1][-1])

