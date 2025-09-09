# Problem: A - Zhan's Blender - https://codeforces.com/gym/633600/problem/A

import math
def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        x, y = map(int, input().split())
        print(math.ceil(n / min(x, y)))

main()