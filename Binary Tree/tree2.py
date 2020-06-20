class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def is_present(node,val1):
    if not node:
        return False
    else:
        if node.value==val1:
            return True
        else:
            return is_present(node.left,val1) or is_present(node.right,val1)

def lca(node,val1,val2):
    temp1=temp2=None
    if not node:
        return None
    else:
        if is_present(node,val1) and is_present(node,val2):
            if node.value==val1 or node.value==val2:
                return node
            else:
                if node.left:
                    temp1=lca(node.left,val1,val2)
                if node.right:
                    temp2=lca(node.right,val1,val2)
                if temp1:
                    return temp1
                elif temp2:
                    return temp2
                else:
                    return node
        else:
          return None


if __name__=="__main__":
    node=Node(12)
    node.left=Node(6)
    node.left.left=Node(4)
    node.left.right=Node(10)
    node.left.left.left=Node(1)
    node.left.left.right=Node(5)
    node.right=Node(22)
    node.right.left=Node(18)
    node.right.right=Node(24)
    node.right.left.right=Node(20)
    node.right.left.left=Node(15)
    print("The lca of 24 and 15 is")
    print(lca(node,24,15).value)


                
