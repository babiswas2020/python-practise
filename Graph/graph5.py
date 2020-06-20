from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def topsort_util(self,visited,stack,u):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.topsort_util(visited,stack,i)
       stack.append(u)
       
   def topsort(self):
       visited=[False]*self.vertex
       stack=[]
       for i in range(self.vertex):
          if not visited[i]:
              self.topsort_util(visited,stack,i)
       print([i for i in stack[::-1]])

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   graph.topsort()

