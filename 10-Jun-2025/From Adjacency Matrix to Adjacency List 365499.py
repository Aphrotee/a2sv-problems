# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

# example below, replace it with your solution
def main():
    n = int(input())
    graph = [[0] for _ in range(n + 1)]

    for node in range(1, n + 1):
        edges = list(map(int, input().split()))
        for i, e in enumerate(edges):
            if e == 1:
                graph[node].append(i + 1)
        graph[node][0] = len(graph[node]) - 1

    for i in range(1, n + 1):
        edges = graph[i]
        print(' '.join(map(str, edges)))

main()