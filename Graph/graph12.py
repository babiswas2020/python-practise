from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def find_shortest_path(self,u,v):
       pre=self.shortest_path(u,v)
       print(pre)
       path=[]
       i=v
       while i!=None:
          path.append(i)
          i=pre[i]
       path=path[::-1]
       print(path)
       if path[0]==u:
          print(f"There is a path from {u} and {v}")
       else:
          print(f"There is no path from {u} and {v}")

   def shortest_path(self,u,v):
       queue=[]
       pre=[None]*self.vertex
       visited=[False]*self.vertex
       queue.append(u)
       visited[u]=True
       while queue:
           m=queue.pop(0)
           for i in self.graph[m]:
              if not visited[i]:
                 visited[i]=True
                 queue.append(i)
                 pre[i]=m
       return pre

if __name__=="__main__":
   graph=Graph(8)
   graph.add_edges(1,2)
   graph.add_edges(1,0)
   graph.add_edges(0,3)
   graph.add_edges(3,7)
   graph.add_edges(3,4)
   graph.add_edges(7,4)
   graph.add_edges(7,6)
   graph.add_edges(4,6)
   graph.add_edges(4,5)
   graph.add_edges(6,5)
   graph.find_shortest_path(0,7)
 
                 
       
      