class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        
        visited = set()     # to check for cycles 

        def dfs(course):
            if course in visited: return False
            elif preMap[course] == []: return True
            
            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre): return False
            
            visited.remove(course)
            preMap[course] = []
            
            return True


        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
