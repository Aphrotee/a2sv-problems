# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        ans = "YES"
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 1:
                ans = "NO"
                break
        print(ans)
main()