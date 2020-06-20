class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def find_max(node):
    left=right=0
    node1=0
    if not node:
       return -99999
    else:
      left=find_max(node.left)
      right=find_max(node.right)
      node1=node.value
      if node1<left:
         node1=left
      if node1<right:
         node1=right
      return node1

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.left.left=Node(4)
   node.left.right=Node(10)
   node.left.left.left=Node(1)
   node.left.left.right=Node(5)
   node.left.left.left.left=Node(29)
   node.right=Node(22)
   node.right.right=Node(24)
   node.right.left=Node(18)
   node.right.left.right=Node(20)
   node.right.left.left=Node(15)
   print(find_max(node))

      