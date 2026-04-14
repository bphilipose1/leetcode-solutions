class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #establish adjMatrix as a dict
        adjMatrix = {i:[] for i in range(numCourses)}

        #load the pairs of key:node, value:list of neighbors
        for p1, p2 in prerequisites:
            adjMatrix[p1].append(p2)

        #perform DFS on graph to check for cycles
        visited = set()
        rec_stack = set()
        courselist = []
        def dfs(cur):
                
            #perform dfs
            #check that current node is not already visited, if it is then skip working on the node, and 
            if cur in visited:
                return True
            
        
            #check that current node is not already in recursion stack, if it is then its a cycle
            if cur in rec_stack:
                return False

            #add that node was processed
            rec_stack.add(cur)

            #call through its neighbors and check for cycles
            for neighbor in adjMatrix[cur]:
                if not dfs(neighbor):
                    return False
            
            rec_stack.remove(cur)
            #when back tracking after completing recursion line, append to course schedule list
            courselist.append(cur)
            visited.add(cur)
            return True


        
        #go through courses 0 to numCourses-1
        for course in range(numCourses):
            #if dfs says there is cycles, return empty array
            if not dfs(course):
                return []

        #if dfs is says no cycles, return the ordered array 
        return courselist
        