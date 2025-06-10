# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

# example below, replace it with your solution
def main():
    n, m = list(map(int, input().split()))
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        graph[u].add(v)
        graph[v].add(u)
    for node in range(2, n + 1):
        if len(graph[node]) != len(graph[node - 1]):
            print("NO")
            return
    
    print("YES")


main()