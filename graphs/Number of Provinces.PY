#https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(n*n)

# Space: O(n)
#appraoch /
""" Use Depth-First Search (DFS) to explore the graph.
Keep a visited array to mark nodes we've already seen.
For every unvisited city, perform DFS and count one more province. """



class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                count += 1

        return count