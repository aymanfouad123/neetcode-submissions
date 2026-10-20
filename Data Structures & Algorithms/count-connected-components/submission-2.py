class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find 
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(node):
            curr = node

            while curr != parent[curr]:
                parent[curr] = parent[parent[curr]]     # path compression
                curr = parent[curr]
            
            return curr
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2: return 0     # didnt perform a union

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        count = n
        for u, v in edges:
            count -= union(u, v)
        
        return count