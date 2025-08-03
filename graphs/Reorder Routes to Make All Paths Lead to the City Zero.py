#https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

# Difficulty:Medium

# Time: O(n)

# Space: O(n)
#appraoch /
"""  Step-by-Step Approach:
Build a set of original directed edges → edges = {(a, b)}.

Build an undirected adjacency list for DFS → each connection a → b contributes a ↔ b in neighbours.

Initialize a visited set and changes counter.

DFS Traversal:

For each neighbor:

If already visited, skip.

If the edge is not pointing toward the current city in the original direction, we increment changes.

Recurse for the neighbor.

Start DFS from city 0.

Return total changes needed. """
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neighbours = {city: [] for city in range(n)}
        changes = 0
        visit = set()

        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):
            nonlocal changes
            for neighbor in neighbours[city]:
                if neighbor in visit:
                    continue
            
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)

        visit.add(0)
        dfs(0)
        return changes