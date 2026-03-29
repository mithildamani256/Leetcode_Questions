class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)

        for course, pre in prerequisites:

            adj[course].append(pre)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True

            visit.add(course)
            
            for pre in adj[course]:
                if not dfs(pre):
                    return False
                adj[pre] = []
            
            visit.remove(course)
            adj[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True