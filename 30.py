from copy import deepcopy


def find_in_vertex(n):
    v = 2 * abs(n) - 2
    if n < 0:
        v += 1
    return v


def find_out_vertex(n):
    v = 2 * abs(n) - 1
    if n < 0:
        v -= 1
    return v


class PermutationGraph:
    def __init__(self, str):
        cycles = [list(map(int, s[:-1].split())) for s in str.split('(')]
        self._n = sum(len(cycle) for cycle in cycles)
        self._graph = [[] for _ in range(2 * self._n)]
        for cycle in cycles:
            self._add_egdes(cycle, self._graph)

    @staticmethod
    def _add_egdes(cycle, graph):
        n = len(cycle)
        for i in range(n):
            j = (i + 1) % n
            in_vertex = find_in_vertex(cycle[j])
            out_vertex = find_out_vertex(cycle[i])
            graph[out_vertex].append(in_vertex)
            graph[in_vertex].append(out_vertex)

    @staticmethod
    def _signed_str(n):
        if n > 0:
            return '+{}'.format(n)
        return str(n)

    def _traverse_cycle(self, v, visited, cycle_nodes):
        visited[v] = 1
        if v % 2 == 0:
            cycle_nodes.append(v // 2 + 1)
        else:
            cycle_nodes.append(-(v // 2) - 1)
        next_v = v - 1 if v % 2 else v + 1
        if visited[next_v]:
            return
        visited[next_v] = 1
        next_v = self._graph[next_v][0]
        if visited[next_v]:
            return
        self._traverse_cycle(next_v, visited, cycle_nodes)

    def __str__(self):
        visited = [0 for _ in range(2 * self._n)]
        permutation = []
        for v in range(2 * self._n):
            if visited[v]:
                continue
            cycle = []
            self._traverse_cycle(v, visited, cycle)
            permutation.append(cycle)
        return ' '.join([
            '({})'.format(' '.join(map(self._signed_str, cycle)))
            for cycle in permutation
            ])

    def __eq__(self, other):
        return list(map(sorted, self._graph)) == \
                list(map(sorted, other._graph))

    def __hash__(self):
        return hash(str(self))

    def two_break(self, u, v, x, y):
        """conduct 2-break between edges (u,v) and (x,y)
        replace edges with (u,x) and (v,y)
        """
        for from_v, to_v in [(u, v), (v, u), (x, y), (y, x)]:
            self._graph[from_v].remove(to_v)
        for from_v, to_v in [(u, x), (x, u), (v, y), (y, v)]:
            self._graph[from_v].append(to_v)

    def graph(self):
        return deepcopy(self._graph)


def main():
    p = PermutationGraph(input())
    u, v, x, y = map(int, input().split(', '))
    p.two_break(u - 1, v - 1, x - 1, y - 1)
    print(p)


if __name__ == '__main__':
    main()

