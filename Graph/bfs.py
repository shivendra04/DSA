from collections import deque

def bfs_of_graph(graph, V):
    visited = [False]*len(graph)
    traversal = []
    for i in range(V):
        if not visited[i]:
            visited[i] = True
            queue = deque([i])
            while queue:
                node = queue.popleft()
                traversal.append(node)
                for neigh in graph[node]:
                    if not visited[neigh]:
                        visited[neigh] = True
                        queue.append(neigh)
    print(traversal)

# --- Hardcoded Input (Typical Problem Format) ---

V = 5
graph = {
    0: [1],
    1: [0],
    2: [3, 4],
    3: [2],
    4: [2],
}

print("BFS Traversal:", bfs_of_graph(graph, V))