class Cell:
   def __init__(self,x,level):
       self.x=x
       self.level=level

def is_valid(x,N):
   if x<0 or x>=N:
      return False
   return True

def step_to_end(pos,N,l):
    queue=[]
    visited=[False]*N
    dx=[1,-1]
    queue.append(Cell(pos,0))
    visited[pos]=True
    while queue:
       m=queue.pop(0)
       if m.x==N-1:
          return m.level
       for i in range(2):
         X=m.x+dx[i]
         if is_valid(X,N) and visited[X]==False:
            queue.append(Cell(X,m.level+1))
            visited[X]=True
       k=[i for i,j in enumerate(l) if j==l[m.x]]
       for i in k:
          if not visited[i]:
             queue.append(Cell(i,m.level+1))

if __name__=="__main__":
   l=[0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
   print(step_to_end(0,len(l),l))
   

       
   

