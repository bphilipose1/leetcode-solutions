from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        MAX_ROW, MAX_COL = len(grid), len(grid[0])
        TOTAL_KEYS = 0
        start_index = (0, 0)
        
        # Parse the grid to find the starting point and total number of keys
        for x in range(MAX_ROW):
            for y in range(MAX_COL):
                if grid[x][y] == '@':
                    start_index = (x, y)
                if 'a' <= grid[x][y] <= 'f':  # Key
                    TOTAL_KEYS += 1
        
        # Represent all keys as a bitmask
        all_keys = (1 << TOTAL_KEYS) - 1  # E.g., if TOTAL_KEYS = 3, all_keys = 0b111
        
        # BFS initialization
        queue = deque([(start_index[0], start_index[1], 0, 0)])  # (x, y, steps, keys_collected)
        visited = set([(start_index[0], start_index[1], 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        while queue:
            x, y, steps, keys = queue.popleft()
            
            # If all keys are collected, return the steps
            if keys == all_keys:
                return steps
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < MAX_ROW and 0 <= ny < MAX_COL:  # Stay within bounds
                    cell = grid[nx][ny]
                    new_keys = keys

                    if cell == '#':  # Wall
                        continue
                    elif 'A' <= cell <= 'F':  # Lock
                        if not (keys & (1 << (ord(cell) - ord('A')))):  # Check if the corresponding key is collected
                            continue
                    elif 'a' <= cell <= 'f':  # Key
                        new_keys |= (1 << (ord(cell) - ord('a')))  # Collect the key

                    # Avoid revisiting the same state
                    if (nx, ny, new_keys) not in visited:
                        visited.add((nx, ny, new_keys))
                        queue.append((nx, ny, steps + 1, new_keys))
        
        # If all keys can't be collected, return -1
        return -1
