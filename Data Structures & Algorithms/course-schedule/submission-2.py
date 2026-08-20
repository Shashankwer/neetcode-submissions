class Solution:
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {}
        for courses in prerequisites:
            current_course = -1
            for index, course in enumerate(courses):
                if index == 0:
                    current_course = course
                    if course not in course_map:
                        course_map[course] = []
                else:
                    if course not in course_map:
                        course_map[course] = []
                    course_map[current_course].append(course)
        def dfs_graph(visited, node):
            #print(node, visited)
            if node in visited:
                return False
            if len(course_map[node]) == 0:
                return True
            visited.add(node)
            result = True
            for n in course_map[node]:
                result = result & dfs_graph(visited, n)
            return result     
        #print(course_map)
        for course in course_map:
            result = True
            for node in course_map[course]:
                visited = set([course])
                result = result & dfs_graph(visited, node)
                if not result:
                    return False
        return True