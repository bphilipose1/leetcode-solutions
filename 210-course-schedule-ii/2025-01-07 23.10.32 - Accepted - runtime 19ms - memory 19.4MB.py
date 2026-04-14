class Solution:
    from collections import defaultdict, deque
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Input:
        prerequisites -> array of (b, a) a {course} and b {prerequisite}
        numCourses -> total courses needed to be completed

        Goals:
        IF POSSIBLE TO GIVE A VALID SOLUTION
            Give a valid instance of a path/order of courses to take (one by one)
        ELSE
            Return []
        
        Cases:
            Case 1:
            1 -> 3 -> 2 -> 4
            Ex Output [1, 3, 2, 4]

            Case 2:
            1 -> 2 -> 4
                 ^
                 |
                 3

            take 1 and 3 first then remove from graph
            order = [1, 3]

            2 -> 4
            
            take 2 next and remove
            order = [1, 3, 2]

            4
            
            now take class 4 and remove
            order = [1, 3, 2, 4]

            no courses/nodes left see if we have a complete solution
            len(order) == numCourses: 
                return order
            else:
                return []


            Ex output [1, 3, 2, 4]

            Case 3 (cycle):
            1 -> 2 -> 4
                ^     |
                |     v
                3 <-  5

            output = [1]

                2 ->  4
                ^     |
                |     v
                3 <-  5

            no other courses with no prereques left check

            len(output) is 1
            numCourses = 5
            return []
            Output []

        '''
        if numCourses <= 0:
            return []
        if numCourses == 1:
            return [numCourses - 1]
        #1. Convert Prerequisites into adjacency dictionary
        preDict = defaultdict(list)

        #2. Create In order array
        in_degree = [0]*numCourses
        for course, prereq in prerequisites:
            preDict[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        output = []
        while queue: #while there is a course with no prerequisite exists
            print(queue)
            cur_course = queue.popleft()
            output.append(cur_course) #record course i was taken

            #remove that course from dependency graph
            #3. Go through the in order array and find courses that at that point have no 
            for neighbor in preDict[cur_course]:
                
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0: #if this now has no prereq add to take course queue
                    queue.append(neighbor)
        
        if len(output) != numCourses:#there exists a cycle
            return []
        else:
            return output

        
        

        

        #- Complete Classes with no prerequisites first -> we can record the in order of each node (EX: Case 2 for node 2 -> in order = 2

        #- If we have no other classes that we can complete at any point
        #    - Did we complete all the classes?
        #        - If yes return class order
        #       - If No we have a cycle
        
        