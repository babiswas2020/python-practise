class Cell:
    def __init__(self,x,y,level):
       self.x=x
       self.y=y
       self.level=level

def is_valid(x,y,N):
    if x>=N or x<=0:
       return False
    if y>=N or y<=0:
        return False
    return True

def knight_tour(pos,tar,N):
    dx=[2,2,-2,-2,1,1,-1,-1]
    dy=[1,-1,-1,1,2,-2,2,-2]
    queue=[]
    visited=[[False for i in range(N)]for i in range(N)]
    queue.append(Cell(pos[0],pos[1],0))
    visited[pos[0]][pos[1]]=False
    while queue:
        m=queue.pop(0)
        if m.x==tar[0] and m.y==tar[1]:
           return m.level
        for i in range(8):
           X=m.x+dx[i]
           Y=m.y+dy[i]
           if is_valid(X,Y,N) and visited[X][Y]!=True:
              queue.append(Cell(X,Y,m.level+1))
              visited[X][Y]=True

if __name__=="__main__":
   print(knight_tour((2,3),(4,5),6))

       
         
    