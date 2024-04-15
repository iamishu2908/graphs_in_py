'''
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.

Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]
Output: 0 2 4 3 1
'''

def dfs(V, adj):
    vis = [False]*V
    out = []
    def recurse(V):
        vis[V] = True
        out.append(V)
        for i in adj[V]:
            if vis[i] == False:
                recurse(i)
    recurse(0)
    return out
V = 5
adj = [[2,3,1] , [0], [0,4], [0], [2]]
print(dfs(V,adj))
        
        