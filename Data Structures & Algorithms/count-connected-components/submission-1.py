class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = defaultdict(list)
        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in nodeMap[node]:
                dfs(nei)

        count = 0

        for node in range(n):
            if node not in visited: 
                dfs(node)
                count += 1

        return count 