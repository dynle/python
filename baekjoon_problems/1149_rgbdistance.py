import sys
def rgbdistance(dp, n, cost):
    for i in range(n):
        if i == 0:
            dp[i][0] = cost[i][0]
            dp[i][1] = cost[i][1]
            dp[i][2] = cost[i][2]
            continue
        # R
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        # G
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        # B
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    min_val = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
    return str(min_val)

n = int(sys.stdin.readline())
cost = []
for _ in range(n):
    colors = list(map(int, sys.stdin.readline().split()))
    cost.append(colors)
dp = [[0]*3 for _ in range(n)]
sys.stdout.write(rgbdistance(dp, n, cost))
