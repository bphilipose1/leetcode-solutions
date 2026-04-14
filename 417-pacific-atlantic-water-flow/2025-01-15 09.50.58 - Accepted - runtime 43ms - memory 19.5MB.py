class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        MAX_ROW, MAX_COL = len(heights), len(heights[0])
        direc = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        #store isPacific and isAtlantic in two matrix for memoization

        pac = [[False] * MAX_COL for _ in range(MAX_ROW)]
        atl = [[False] * MAX_COL for _ in range(MAX_ROW)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in direc:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < MAX_ROW and 0 <= nc < MAX_COL and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        pacific = []
        atlantic = []

        for c in range(MAX_COL):
            pacific.append((0, c))
            atlantic.append((MAX_ROW - 1, c))

        for r in range(MAX_ROW):
            pacific.append((r, 0))
            atlantic.append((r, MAX_COL - 1))
        
        #mark for pac
        bfs(pacific, pac)
        
        #mark for atl
        bfs(atlantic, atl)
        res = []
        for r in range(MAX_ROW):
            for c in range(MAX_COL):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
