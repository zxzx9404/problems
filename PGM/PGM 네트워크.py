def solution(n, computers):
    answer = n
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] and i != j and find_parent(i) != find_parent(j):
                union(i, j)
                answer -= 1              

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))