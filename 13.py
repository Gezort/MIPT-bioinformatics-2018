import sys

sys.setrecursionlimit(10000)

ALPHABET = 'ACGT'


def dfs(cur_vertex, graph, visited_set):
    max_depth = 0
    best_end = []
    visited_set.add(cur_vertex)
    for next_vertex in graph[cur_vertex]:
        if next_vertex not in visited_set:
            depth, end = dfs(next_vertex, graph, visited_set)
            if depth > max_depth:
               max_depth = depth
               best_end = end
            visited_set.remove(next_vertex)
    return max_depth + 1, [cur_vertex] + best_end


def collect_result(kmers_chain, k, d):
    kmers_chain = [kmer.split('#') for kmer in kmers_chain]
    res = [kmers_chain[0][0]]
    for i in range(d):
        res.append(kmers_chain[i + 1][0][-1])
    res.append(kmers_chain[0][1])
    for _, kmer in kmers_chain[1:]:
        res.append(kmer[-1])
    return ''.join(res)


def main():
    k, d = map(int, input().split())
    kmers = sys.stdin.read().strip().split('\n')
    kmers = [kmer.split('|') for kmer in kmers]
    n = len(kmers) + 2 * k + d - 1

    edges = {}
    for l, r in kmers:
        edges[l + '#' + r] = []
    for l, r in kmers:
        cur_kmer = l + '#' + r
        for x in ALPHABET:
            for y in ALPHABET:
                next_kmer = l[1:] + x + '#' + r[1:] + y
                if next_kmer not in edges:
                    continue
                edges[cur_kmer].append(next_kmer)

    for l, r in kmers:
        cur_kmer = l + '#' + r
        depth, best_chain = dfs(cur_kmer, edges, set())
        if depth == len(kmers):
            print(collect_result(best_chain, k, d))
            break


if __name__ == '__main__':
    main()
