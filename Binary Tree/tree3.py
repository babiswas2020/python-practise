class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None


def min(node):
    if not node:
       return None
    while node.left!=None:
        node=node.left
    return node


def max(node):
  if not node:
     return None
  while node.right!=None:
       node=node.right
  return node
    


def search(node,val1):
   temp1=temp2=None
   if not node:
      return None
   else:
      if node.value==val1:
         return node
      else:
         if node.left:
           temp1=search(node.left,val1)
         if node.right:
           temp2=search(node.right,val1)
         if temp1:
            return temp1
         elif temp2:
             return temp2
         else:
             return None

def inorder_sucessor_util(node,node1):
    temp1=temp2=None
    if node.left==node1:
       return node
    else:
       if node.left:
          temp1=inorder_sucessor_util(node.left,node1)
       if node.right:
          temp2=inorder_sucessor_util(node.right,node1)
       if temp1:
          return temp1
       elif temp2:
          return temp2
       else:
          return node 
         
def inorder_sucessor(node,node1):
    if not node:
       return None
    else:
        if node1.right:
           return min(node1.right)
        else:
           if node==node1:
              return None
           elif max(node)==node1:
              return None
           else:
              return inorder_sucessor_util(node,node1)

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.right=Node(22)
   node.left.left=Node(4)
   node.left.right=Node(10)
   node.right.left=Node(18)
   node.right.right=Node(24)
   node.right.left.left=Node(15)
   node.right.left.right=Node(20)
   node.left.left.left=Node(1)
   node.left.left.right=Node(5)
   print("Find the adress of 18")
   node2=search(node,18)
   print(node2.value)
   print("Find the inorder sucessor of 18")
   print(inorder_sucessor(node,node2).value)


    