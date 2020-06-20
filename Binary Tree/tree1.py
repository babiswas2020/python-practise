class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def height(node):
   count=0
   queue=[]
   queue.append(node)
   while queue:
      q_len=len(queue)
      if q_len:
        count=count+1
      while q_len:
          m=queue.pop(0)
          if m.left:
             queue.append(m.left)
          if m.right:
             queue.append(m.right)
          q_len=q_len-1
   return count
      
   
def diameter(node):
    d1=d2=0
    h1=h2=0
    if not node:
       return 0
    else:
       if node.left:
          h1=height(node.left)
       if node.right:
          h2=height(node.right)
       if node.left:
          d1=diameter(node.left)
       if node.right:
          d2=diameter(node.right)
       return max(h1+h2+1,max(d1,d2))

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.right=Node(22)
   node.left.right=Node(10)
   node.left.left=Node(4)
   node.left.left.left=Node(1)
   node.left.left.right=Node(5)
   node.right.left=Node(18)
   node.right.right=Node(24)
   node.right.left.right=Node(20)
   node.right.left.left=Node(15)
   print(diameter(node))


