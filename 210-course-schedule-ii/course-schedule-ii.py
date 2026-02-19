class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        visited = set()

        output = []

        def dfs(crs):
            if crs in visit:
                return False
            
            if crs in visited:
                return True
            
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)

            visited.add(crs)

            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output

        

        
        

        