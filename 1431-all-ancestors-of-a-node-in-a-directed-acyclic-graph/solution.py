class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjDict = {}
        for val in range(n): #initialize each node
            adjDict[val] = []

        for fromNode, toNode in edges:
            adjDict[toNode].append(fromNode)

        memo = {}

        def dfs(value):
            #goal is to return the all the ancecstors for that value
            if value in memo:
                return memo[value]
            
            ancestors = set()
            
            for parent in adjDict[value]:
                ancestors.add(parent)
                ancestors.update(dfs(parent))
            
            memo[value] = ancestors
            return ancestors
        

        
        result = []
        for i in range(n):
            ancestors = dfs(i)

            result.append(sorted(ancestors))
        
        return result