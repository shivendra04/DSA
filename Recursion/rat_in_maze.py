def rat_in_maze(i,j,di,dj,maze,row,ans,visited,path):
    if i == row-1 and j == row-1:
        ans.append(path)
        return

    directions = "DLRU"
    for ind in range(4):
        next_i = i+di[ind]
        next_j = j+dj[ind]
        if next_i>=0 and next_j>=0 and next_i<row and next_j<row and visited[next_i][next_j] != 1 and maze[next_i][next_j] == 1:
            visited[i][j] = 1
            rat_in_maze(next_i,next_j,di,dj,maze,row,ans,visited,path+directions[ind])
            visited[i][j] = 0


def main():
    maze =  [
             [1, 0, 0, 0],
             [1, 1, 0, 1],
             [1, 1, 0, 0],
             [0, 1, 1, 1]
             ]
    row = len(maze)
    ans = []
    visited = [[0 for _ in range(row)]for _ in range(row)]
    di = [+1, 0, 0, -1]
    dj = [0, -1, +1, 0]
    if maze[0][0] == 1:
        rat_in_maze(0,0,di, dj,maze, row, ans, visited, "")
    print(ans)

main()