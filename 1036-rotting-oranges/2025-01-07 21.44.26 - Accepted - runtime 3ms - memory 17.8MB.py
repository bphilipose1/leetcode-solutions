class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #1. Fully run through matrix 
        #    - To initialize fresh_orange
        #    initialize queue ->
        #    q = [(0, (0,1))]
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        orange_queue = deque()
        fresh_orange = 0
        total_time = 0
        visited_oranges = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh_orange += 1
                if grid[x][y] == 2:
                    orange_queue.append((0, (x, y)))

        #2. Perform BFS
        while orange_queue:
        
            #    Dequeue -> time, x, y  = q.pop()
            time, coord = orange_queue.popleft()
            x_coord, y_coord = coord     

            if coord in visited_oranges: #already processed this orange move on
                continue

            #    Mark current cell as rotton orange -> visited_oranges.add((x, y))
            visited_oranges.add(coord)

            #    fresh_orange -= 1
            if grid[x_coord][y_coord] != 2:
                grid[x_coord][y_coord] = 2
                fresh_orange -= 1

            #    Append Potential Oranges to now get rotten ->
            #        if (x+1, y) or (x-1, y) or (x, y+1) or (x, y-1) is fresh_orange add to queue
            #            q.append(time + 1, (next_x, next_y))
            x=x_coord
            y=y_coord

            old_len = len(orange_queue)
            if MAX_ROW > x+1 >= 0 and grid[x+1][y] == 1:
                orange_queue.append((time+1, (x+1, y)))
            if MAX_ROW > x-1 >= 0 and grid[x-1][y] == 1:
                orange_queue.append((time+1, (x-1, y)))
            if MAX_COL > y+1 >= 0 and grid[x][y+1] == 1:
                orange_queue.append((time+1, (x, y+1)))
            if MAX_COL > y-1 >= 0 and grid[x][y-1] == 1:
                orange_queue.append((time+1, (x, y-1)))
            
            if old_len == len(orange_queue):# if there are no new oranges to still explore that arent rotton
                total_time = max(total_time, time)
                
                
        
        if fresh_orange != 0:
            return -1
        else:
            return total_time

#        if there are no next targets, check if current time is maxTime path/branch
#        total_min = max(total_min, time)

#    if fresh_oranges != 0:
#        return -1
#    else:
#        return max_time    

'''

min0        min1      min2
[1 2 1] -> [2 2 2] -> [2 2 2]
[1 0 1]    [1 0 1]    [2 0 2]
[0 1 0]    [0 1 0]    [0 1 0]
q = [(1, 00), (1, 02)]
visited_oranges = ((01))
fresh_orange_counter = 5


Output: -1

min0        min1    min2
[1 2 1] -> [2 2 2]  [2 2 2]
[1 1 1]    [1 2 1]  [2 2 2]
[0 2 0]    [0 2 0]  [0 2 0]

Rotting Behavior: 
- Only happens to cells that are 1 CELL [Above, Below, Left, Right] of a rotting orange each minute
- Use BFS traversal to act as infecting neighbors each minutes

- Check if there are no good oranges left? Yes -> return -1 else: return number of minutes for all oranges to become rotten

Solution
1. Fully run through matrix 
    - To initialize fresh_orange

    initialize queue ->
    q = [(0, (0,1))]
2. Perform BFS
    Dequeue -> time, x, y  = q.pop()
    Mark current cell as rotton orange -> visited_oranges.add((x, y))
    fresh_orange -= 1

    Append Potential Oranges to now get rotten ->
        if (x+1, y) or (x-1, y) or (x, y+1) or (x, y-1) is fresh_orange add to queue
            q.append(time + 1, (next_x, next_y))
        if there are no next targets, check if current time is maxTime path/branch
        total_min = max(total_min, time)

    if fresh_oranges != 0:
        return -1
    else:
        return max_time

variables:
    fresh_orange: counter to record current amount of non rotten oranges (each conversion to rotten deducts one from counter) O(n*m)
    total_min: minute counter to record how many rotting iterations occured.
    visited_oranges: Represents oranges that are already rotten/have become rotten already
    queue: Represents oranges that now are targets of becoming rotten (before appending check that orange at cell isnt already rotten/in visited_oranges) 







?.  If fresh_orange != 0:
        return -1
    return total_min

Problem Outline:
0 -> Empty Space
1 -> Orange
2 -> Rotten Orange

Q: Can there be more than one rotton orange in the matrix or no rotton orange
A: Yes rotton_orange >= 0

Q: Since the spread is to neighbors first, would BFS be an appropriate approach?
A: That sounds good

Q: If the number of good oranges is not 0 then we return 01
A: Yes thats correct

Q: Is rotting of oranges surrounding a rotten orange simotaneous or incremental?
A: It is simotaneous

Q: Do two rotting oranges as neighbors to a good orange speed the rotting time?
A: No it is the same time


At each minute ANY ORANGE (ABOVE/BELOW/LEFT/RIGHT) of a rotton orange becomes rotton



[[2,1,1],
 [1,1,0],
 [0,1,1]]

'''