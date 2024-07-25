# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/520688/problem/B

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def count_trees(graph):
    n = len(graph)
    visited = [False] * n
    tree_count = 0

    for node in range(n):
        if not visited[node]:
            dfs(node, visited, graph)
            tree_count += 1

    return tree_count

def construct_graph(p):
    n = len(p)
    graph = [[] for _ in range(n)]

    for i in range(n):
        relative = p[i] - 1
        graph[i].append(relative)
        graph[relative].append(i)

    return graph

def solve():
    num_baboons = int(input())
    distant_relatives = list(map(int, input().split()))

    graph = construct_graph(distant_relatives)

    num_trees = count_trees(graph)
    return num_trees

t = 1
# t = int(input())
for _ in range(t):
    print(solve())
