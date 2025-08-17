# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

from collections import defaultdict
def main():
  H, W = list(map(int, input().split()))
  a = []
  MOD = 7 + pow(10, 9)
  
  for _ in range(H):
    w = input().strip()
    a.append(w)
  
  
  dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
  
  dp[1][1] = 1
  for i in range(1, H + 1):
    for j in range(1, W + 1):
      if i == 1 and j == 1:
        continue
      if a[i - 1][j - 1] == "#":
        dp[i][j] = 0
      else:
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
  return dp[-1][-1] % MOD
print(main())