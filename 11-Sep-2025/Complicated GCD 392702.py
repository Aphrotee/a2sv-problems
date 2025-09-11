# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

def main():
    a, b = list(map(int, input().split()))
    print(a if a == b else 1)

if __name__ == "__main__":
    main()