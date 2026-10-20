class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        unvisited, visiting, completed = 0, 1, 2
        state = [unvisited] * numCourses
         
        def dfs(i):
            if state[i] == visiting: return False
            if state[i] == completed:
                return True
            
            state[i] = visiting

            for pre in preMap[i]:
                if not dfs(pre): return False
            
            state[i] = completed
            result.append(i)
            return True

        result = []
        for i in range(numCourses):
            if not dfs(i): 
                return []

        return result
