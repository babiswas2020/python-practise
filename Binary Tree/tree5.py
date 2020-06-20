class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def distance(node,node1):
    temp1=temp2=0
    if not node:
       return -1
    if node==node1:
       return 0
    else:
        temp1=distance(node.left,node1)
        temp2=distance(node.right,node1)
        if temp1>=0:
           return temp1+1
        elif temp2>=0:
           return temp2+1
        else:
           return -1
        
if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.left.right=Node(10)
   node.left.left=Node(4)
   node.left.left.left=Node(1)
   node.left.left.right=Node(5)
   node.right=Node(22)
   node.right.left=Node(18)
   node.right.left.right=Node(20)
   node.right.left.left=Node(15)
   node.right.right=Node(24)
   print("The distance between root and node 24 is")
   print(distance(node,node.right.right))

    