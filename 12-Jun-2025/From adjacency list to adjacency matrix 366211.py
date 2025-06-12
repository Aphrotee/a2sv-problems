# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

# example below, replace it with your solution
def main():
    n = int(input())

    graph = [[0 for _ in range(n)] for _ in range(n)]

    for node in range(n):
        line = list(map(int, input().split()))
        for neigh in line[1:]:
            graph[node][neigh - 1] = 1


    for edges in graph:
        print(' '.join(map(str, edges)))
main()