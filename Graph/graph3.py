from collections import defaultdict

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)

   def DFS(self,u):
      stack=[]
      visited=[False]*self.vertex
      stack.append(u)
      while stack:
         m=stack.pop()
         if not visited[m]:
            print(m)
            visited[m]=True
         for i in self.graph[m]:
            if not visited[i]:
               stack.append(i)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(0,1)
   graph.add_edges(3,3)
   graph.DFS(2)


      