class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Create a graph representations either using dictionary or adjacency matrix

        #the dictionary will hold the neighbors of each key
        adjMatrix = {i: [] for i in range(numCourses)}
        
        for pairs in prerequisites:
            adjMatrix[pairs[0]].append(pairs[1])
        
        print(adjMatrix)


        #check graph for cycles using depth first search to find cycles
        start = int(prerequisites[0][0])
        visited = set()
        rec_stack = set()
        def cycleCheck(cur):
            
            #check if current value is already in line to be checked, if so its a cycle
            if cur in rec_stack:
                return True
            #check if current value has already been visited before, then it is not in cycle, because its not a direct descendant
            if cur in visited:
                return False
            
            #add that current node has been visited
            visited.add(cur)
            rec_stack.add(cur)

            #go deeper by checking all its neighbors
            for neighbor in adjMatrix[cur]:
                if cycleCheck(neighbor):
                    return True
            
            #checked all its descendants at this point time to return
            rec_stack.remove(cur)
            return False

        if cycleCheck(start):
            return False
        return True

