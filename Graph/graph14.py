class Cell:
   def __init__(self,x,y,level):
       self.x=x
       self.y=y
       self.level=level

def is_valid(x,y,Mrr,N):
    if x>=N or x<0:
       return False
    if y>=N or y<0:
       return False
    if Mrr[x][y]=='X':
       return False
    return True

def find_steps(pos,tar,Mrr,N):
   dx=[1,-1,0,0]
   dy=[0,0,1,-1]
   queue=[]
   queue.append(Cell(pos[0],pos[1],0))
   visited=[[False for i in range(N)] for i in range(N)]
   visited[pos[0]][pos[1]]=True
   while queue:
       m=queue.pop(0)
       if m.x==tar[0] and m.y==tar[1]:
           return m.level
       for i in range(4):
          X=m.x+dx[i]
          Y=m.y+dy[i]
          if is_valid(X,Y,Mrr,N) and Mrr[X][Y]!='X':
             if not visited[X][Y]:
                queue.append(Cell(X,Y,m.level+1))
                visited[X][Y]=True

if __name__=="__main__":
  N=4
  Mrr=[[3,3,1,'X'],[3,'X',3,3],['E',3,'X',3],['X',3,3,3]]
  pos=[0,2]
  print(find_steps(pos,[2,0],Mrr,4))


      