# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    if k == 0:
        if nums[k] - 1 < 1:
            print(-1)
        else:
            print(nums[k] - 1)
    elif k == n:
        print(nums[k - 1])
    elif k < n and nums[k - 1] != nums[k]:
        print(nums[k - 1])
    else:
        print(-1)
main()