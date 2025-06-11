# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

# example below, replace it with your solution
def main():
    n = int(input())
    count = 0

    for node in range(1, n + 1):
        edges = list(map(int, input().split()))
        for i, e in enumerate(edges):
            if e == 1:
                count += 0.5
    print(int(count))


main()