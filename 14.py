import sys


def extract_vertices(kmers, k):
    vertex_set = {kmer[:k - 1] for kmer in kmers} | {kmer[1:] for kmer in kmers}
    return {v: i for i, v in enumerate(vertex_set)}


def build_graph(kmers, k, vertices):
    n = len(vertices)
    edges = [[] for _ in range(n)]
    for kmer in kmers:
        fr = vertices[kmer[:k - 1]]
        to = vertices[kmer[1:]]
        edges[fr].append(to)
    return edges


def find_max_nonbranching_paths(edges):
    n = len(edges)
    in_degs = [0 for _ in range(n)]
    for out_edges in edges:
        for v in out_edges:
            in_degs[v] += 1
    out_degs = [len(out_edges) for out_edges in edges]

    nonbranching_paths = []
    for v in range(n):
        if in_degs[v] == 1 and out_degs[v] == 1:
            continue
        if out_degs[v] == 0:
            continue
        for to in edges[v]:
            path = [v, to]
            next = to
            while in_degs[next] == 1 and out_degs[next] == 1:
                next = edges[next][0]
                path.append(next)
                if len(path) == n: # cycle encountered
                    break
            nonbranching_paths.append(path)
    return nonbranching_paths


def main():
    kmers = [line.strip() for line in sys.stdin.readlines()]
    k = len(kmers[0])
    vertices = extract_vertices(kmers, k)
    descriptors = {i: v for v, i in vertices.items()}
    edges = build_graph(kmers, k, vertices)
    nonbranching_paths = find_max_nonbranching_paths(edges)
    contigs = []
    for path in nonbranching_paths:
        contig = descriptors[path[0]] + ''.join([descriptors[v][-1] for v in path[1:]])
        contigs.append(contig)
    print(*contigs)


if __name__ == '__main__':
    main()
