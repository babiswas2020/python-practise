from collections import defaultdict

class Graph:
   def __init__(self,value):
       self.value=value
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)
       self.graph[v].append(u)

   def t_closure_util(self,M,u,v):
       M[u][v]=1
       for i in self.graph[v]:
          if M[u][i]!=1:
             self.t_closure_util(M,u,i)

   def transitive_closure(self):
       M=[[-1 for i in range(self.vertex)]for i in range(self.vertex)]
       for i in range(self.vertex):
           self.t_closure_util(M,i,i)
       print(M)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.transitive_closure()

