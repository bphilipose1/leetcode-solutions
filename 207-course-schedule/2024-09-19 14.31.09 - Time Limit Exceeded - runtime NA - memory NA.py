class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Create a graph representations either using dictionary or adjacency matrix

        #the dictionary will hold the neighbors of each key
        adjMatrix = {i: [] for i in range(numCourses)}
        
        for p1, p2 in prerequisites:
            adjMatrix[p1].append(p2)
        
        print(adjMatrix)


        #check graph for cycles using depth first search to find cycles

        visiting = set()
        def cycleCheck(cur):
            
            #check if current value is already in line to be checked, if so its a cycle
            if cur in visiting:
                return True
            #check if current value has already been visited before, then it is not in cycle, because its not a direct descendant
            if adjMatrix[cur] == []:
                return False
            
            #add that current node has been visited

            visiting.add(cur)

            #go deeper by checking all its neighbors
            for neighbor in adjMatrix[cur]:
                if cycleCheck(neighbor):
                    return True
            
            #checked all its descendants at this point time to return
            visiting.remove(cur)
            return False

        for courses in range(numCourses):
            if cycleCheck(courses):
                return False
        return True

