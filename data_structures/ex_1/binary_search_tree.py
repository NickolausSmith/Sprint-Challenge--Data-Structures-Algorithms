class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #Recursive:
    
    cb(self.value) # call the cb on the current node
    
    if self.left: # check if this node has a left child
      self.left.depth_first_for_each(cb)     # call DFS on the left child
      
    if self.right: # check if this node has a right child
      self.right.depth_first_for_each(cb)    # call DFS on the right child

    #Iterative
    
    stack = [] # initialize a list to be our stack
    stack.append(self) # add the root node to the stack
    
    while len(stack): # loop as long as we have elements in the stack
      current_node = stack.pop()  # pop off the stack
     
      if current_node.right:  # check if the popped-off node has a right child
        stack.append(current_node.right)  # add the right child to the stack
        
      if current_node.left: # check if the popped-off node has a left child
        stack.append(current_node.left)  # add the left child to the stack
          
        cb(current_node.value) # invoke the cb on the popped-off node

  def breadth_first_for_each(self, cb):
    # Iterative implementation
    stack = [] # initialize a list to be our stack
    stack.append(self) # add the root node to the stack

    while len(stack): #pop off the stack
      current_node = stack.pop() # check if the popped-off node has a left child

      if current_node.right: # check if the popped off node has a right child
        stack.append(current_node.right) # add the right child to the stack

      if current_node.left: # check if the popped-off node has a left child
        stack.append(current_node.left) # add the left child to the stack
        
    cb(current_node.value) # invoke the cb on the popped-off node


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
