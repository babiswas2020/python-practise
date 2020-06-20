from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def addedge(self,u,v):
     self.graph[u].append(v)

   def IDDFS(self,src,target,maxdepth):
      for i in range(maxdepth):
         if self.DLS(src,target,i):
            return True
      return False

   def DLS(self,src,target,maxdepth):
       if src==target:
          return True
       if maxdepth<=0:
          return True
       for i in self.graph[src]:
          if self.DLS(i,target,maxdepth-1):
              return True
       return False

if __name__=="__main__":
   graph=Graph(7)
   graph.addedge(0,1)
   graph.addedge(0,2)
   graph.addedge(1,3)
   graph.addedge(1,4)
   graph.addedge(2,5)
   graph.addedge(2,6)
   if graph.IDDFS(0,6,3):
      print("Target reachable")
   else:
      print("Target is not reachable")


   