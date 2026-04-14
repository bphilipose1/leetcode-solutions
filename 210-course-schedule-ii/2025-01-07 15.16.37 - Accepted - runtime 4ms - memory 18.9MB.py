class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize graph and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build graph and in-degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize queue with courses having 0 in-degree
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        order = []
        while q:
            cur_node = q.popleft()
            order.append(cur_node)

            # Reduce in-degree for neighboring courses
            for neighbor in graph[cur_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # If all courses are processed, return the order
        if len(order) == numCourses:
            return order
        else:
            return []