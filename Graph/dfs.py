def dfs_helper(graph, node, visited, traversal):
    visited[node] = True
    traversal.append(node)
    for neigh in graph[node]:
        if not visited[neigh]:
            dfs_helper(graph, neigh, visited, traversal)

def dfs_of_graph(V, graph):
    visited = [False]*V
    traversal = []
    for i in range(V):
        if visited[i] is False:
            dfs_helper(graph, i, visited, traversal)
    print(traversal) 



# --- Same Hardcoded Input ---
V = 5
graph = {
    0: list((1,)),
    1: list((0,)),
    2: list((3, 4)),
    3: list((2,)),
    4: list((2,)),
}

print("DFS Traversal (Recursive):", dfs_of_graph(V, graph))