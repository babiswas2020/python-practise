class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def find_common_node(self,node1):
       stack1=[]
       stack2=[]
       node2=self
       while True:
          if node1:
             stack1.append(node1)
             node1=node1.left
          elif node2:
             stack2.append(node2)
             node2=node2.left
          elif stack1 and stack2:
             node1=stack1[-1]
             node2=stack2[-1]
             if node1.value==node2.value:
                print(node1.value)
                stack1.pop()
                stack2.pop()
                node1=node1.right
                node2=node2.right
             elif node1.value>node2.value:
                node1=None
                stack2.pop()
                node2=node2.right
             elif node1.value<node2.value:
                node2=None
                stack1.pop()
                node1=node1.right
          else:
             break

                
           
   def insert(self,value):
       if self.value>value:
          if self.left:
             self.left.insert(value)
          else:
             self.left=Node(value)
       elif self.value<value:
          if self.right:
             self.right.insert(value)
          else:
             self.right=Node(value)
       else:
           print("Duplication not allowed")

if __name__=="__main__":
   print("Constructing Tree1")
   node=Node(12)
   node.insert(22)
   node.insert(18)
   node.insert(24)
   node.insert(15)
   node.insert(20)
   node.insert(6)
   node.insert(10)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   print("Constructing Tree2")
   node1=Node(14)
   node1.insert(21)
   node1.insert(20)
   node1.insert(18)
   node1.insert(15)
   node1.insert(12)
   node1.insert(7)
   node1.insert(10)
   node1.insert(5)
   print("Displaying the common nodes")
   node.find_common_node(node1)
   
