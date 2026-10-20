class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        nodeMap = defaultdict(list)
        
        # making and adj list
        for node, child in edges:
            nodeMap[node].append(child)
            nodeMap[child].append(node)
        
        def dfs(node, parent):
            if node in visited: return False

            visited.add(node)

            for child in nodeMap[node]:
                if child == parent: continue
                if not dfs(child, node): return False
        
            return True 

        return dfs(0, -1) and len(visited) == n