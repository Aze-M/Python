edges1 = [[1,2],[2,3],[4,2]]
edges2 = [[1,2],[5,1],[1,3],[1,4]]

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        nodemap = {}

        for node in edges:
            if node[0] in nodemap:
                nodemap[node[0]] +=1
                
            if node[1] in nodemap:
                nodemap[node[1]] +=1

            if node[0] not in nodemap:
                nodemap[node[0]] = 1

            if node[1] not in nodemap:
                nodemap[node[1]] = 1
        
            if nodemap[node[0]] == len(edges):
                return node[0]
            
            elif nodemap[node[1]] == len(edges):
                return node[1]
                

sol = Solution

print(sol.findCenter(sol,edges1))
print(sol.findCenter(sol,edges2))