class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def leaf_nodes(node):
   def is_leaf(node):
      if not node:
         return False
      elif node.left==None and node.right==None:
         return True
      else:
         return False
   stack=[]
   stack.append(node)
   temp=None
   while stack:
       temp=stack.pop()
       while temp and (not is_leaf(temp)):
            if temp.left:
               stack.append(temp.left)
            if temp.right:
               stack.append(temp.right)
            temp=stack.pop()
       if temp:
          if is_leaf(temp):
              print(temp.value)

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
   node.right.right=Node(24)
   node.right.left.left=Node(15)
   print(leaf_nodes(node))



