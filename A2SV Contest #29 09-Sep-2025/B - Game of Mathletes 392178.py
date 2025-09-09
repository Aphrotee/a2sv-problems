# Problem: B - Game of Mathletes - https://codeforces.com/gym/633600/problem/B

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))

        nums.sort()
        score = 0

        l = 0
        r = n - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                score += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            elif total > k:
                r -= 1
        print(score)
main()      