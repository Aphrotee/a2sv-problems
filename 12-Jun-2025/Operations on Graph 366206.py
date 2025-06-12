# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    k = int(input())
    for _ in range(k):
        operation = list(map(int, input().split()))
        if operation[0] == 1:
            u, v = operation[1], operation[2]
            graph[u].append(v)
            graph[v].append(u)
        elif operation[0] == 2:
            u = operation[1]
            print(' '.join(map(str, graph[u])))
main()