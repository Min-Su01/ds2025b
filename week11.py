graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]
#dfs(깊이 우선 탐색): 모든 노드를 방문하는 방법
#깊이 우선 탐색이 너비 우선 탐색보다 좀 더 간단하다. (속도는 너비가 더 빠르다)
def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

visited_dfs = [0 for _ in range(len(graph))]
dfs(graph, 7, visited_dfs) #정점 7, 즉 'H'에서 탐색을 시작한다는 뜻.