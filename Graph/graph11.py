from collections import defaultdict
import sys

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def find_level(self,u,level):
       count=0
       visited=[False]*self.vertex
       queue=[]
       queue.append(u)
       visited[u]=True
       while queue:
          print(queue)
          q_len=len(queue)
          if q_len:
             count=count+1
             if count==level:
               print(queue)
          while q_len:
             m=queue.pop(0)
             for i in self.graph[m]:
               if not visited[i]:
                  queue.append(i)
                  visited[i]=True
             q_len=q_len-1

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   le=int(sys.argv[1])
   graph.find_level(2,le)


   

          