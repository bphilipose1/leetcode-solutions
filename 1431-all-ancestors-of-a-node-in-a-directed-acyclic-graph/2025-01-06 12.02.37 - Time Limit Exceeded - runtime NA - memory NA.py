class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjDict = {}
        for val in range(n): #initialize each node
            adjDict[val] = []

        for fromNode, toNode in edges:
            adjDict[toNode].append(fromNode)


        def dfs(value):
            #goal is to return the all the ancecstors for that value
            sub_array = []
            
            for sub_value in adjDict[value]:
                sub_array += [sub_value]
                sub_array += dfs(sub_value)
            
            return sub_array
        

        fin_result = [[] for _ in range(n)]

        for i in range(n):
            x = list(set(dfs(i)))

            fin_result[i] = sorted(x)
        
        return fin_result