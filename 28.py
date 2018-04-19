import sys

def str_to_in_vertex(s):
    v = 2 * abs(eval(s)) - 2
    if s[0] == '-':
        v += 1
    return v


def str_to_out_vertex(s):
    v = 2 * abs(eval(s)) - 1
    if s[0] == '-':
        v -= 1
    return v


def add_egdes(permutation, graph):
    n = len(permutation)
    for i in range(n):
        j = (i + 1) % n
        out_vertex = str_to_out_vertex(permutation[i])
        in_vertex = str_to_in_vertex(permutation[j])
        graph[out_vertex].append(in_vertex)
        graph[in_vertex].append(out_vertex)


def split_into_cycles(str):
    return [s[:-1].split() for s in str.split('(')]


def dfs(graph, v, visited):
    visited[v] = 1
    for u in graph[v]:
        if not visited[u]:
            dfs(graph, u, visited)


def main():
    sys.setrecursionlimit(100000)
    p = split_into_cycles(input())
    q = split_into_cycles(input())
    n = sum(len(cycle) for cycle in p)
    graph = [[] for _ in range(2 * n)]
    for cycle in p:
        add_egdes(cycle, graph)
    for cycle in q:
        add_egdes(cycle, graph)
    visited = [0 for _ in range(2 * n)]
    dist = n
    for v in range(2 * n):
        if visited[v]:
            continue
        dfs(graph, v, visited)
        dist -= 1
    print(dist)


if __name__ == '__main__':
    main()

