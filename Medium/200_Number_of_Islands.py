class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            que = collections.deque()
            visited.add((r,c))
            que.append((r,c))

            while que:
                row, col = que.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(ROWS) and c in range(COLS) and grid[r][c]=='1' and (r,c) not in visited):
                        que.append((r,c))
                        visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
