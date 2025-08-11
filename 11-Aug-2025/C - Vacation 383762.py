# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

def main():
  n = int(input())
  vacations = []
  
  dp = [[0,0,0]]
  for _ in range(n):
    v = list(map(int, input().split()))
    vacations.append(v)
  for i in range(n):
    vacay = []
    for j in range(3):
      vacay.append(vacations[i][j] + max(dp[i][j - 1], dp[i][j - 2]))
    dp.append(vacay)
  return max(dp[n])
# t = int(input())
# for _ in range(t):
#  print(main())
print(main())