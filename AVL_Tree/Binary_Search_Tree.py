class Binary_Search_Tree:

  class __BST_Node:
  
    def __init__(self, value): 
      self.value = value
      self.left = None
      self.right = None 
      self.height = 1

  def __init__(self):
    self.__root = None
    self.__height = 0

  def insert_element(self, value):
    insert_node = self.__BST_Node(value) 
    self.__root = self.__recursive_insert(insert_node, self.__root, value) 
    self.__height = self.__root.height 

  def __recursive_insert(self, Node, t, value): 
    if t == None: 
      return Node
    
    if value == t.value:
      raise ValueError
    
    elif Node.value < t.value: 
      t.left = self.__recursive_insert(Node, t.left, value)
      self.__update_height(t)

    elif Node.value > t.value: 
      t.right = self.__recursive_insert(Node,t.right, value)
      self.__update_height(t)
    
    return self.__balance(t) 
    
  def __update_height(self, t): 
    if t.left == None and t.right == None:
      t.height = 1
    elif t.left == None and t.right != None: 
        t.height = t.right.height + 1
    elif t.right == None and t.left != None: 
        t.height = t.left.height + 1
    else: 
        t.height = max(t.left.height, t.right.height) + 1

  def remove_element(self, value): 
    self.__root = self.__recursively_remove_element(self.__root , value) 
  
  def __recursively_remove_element(self, Node, value): 
    if Node == None: 
      raise ValueError
    
    elif Node.value == value: 
      if Node.right == None and Node.left == None: 
        return None
      elif Node.right == None: 
        return Node.left
      elif Node.left == None: 
        return Node.right
      else: 
        counter_node = Node.right
        while counter_node.left != None:
          counter_node = counter_node.left
        Node.right = self.__recursively_remove_element(Node.right, counter_node.value)
        Node.value = counter_node.value

    elif value < Node.value: 
      Node.left = self.__recursively_remove_element(Node.left, value)
      self.__update_height(Node)

    elif value > Node.value: 
      Node.right = self.__recursively_remove_element(Node.right, value)
      self.__update_height(Node)
      
    return self.__balance(Node)

  def in_order(self):   
    if self.__root == None:
      return '[ ]'
    in_order = self.__recursive_in_order(self.__root) 
    return '[' + in_order[:-1] + ' ]'

  def __recursive_in_order(self, Node): 
    if Node == None:
      return ''
    string = ''
    string += str(self.__recursive_in_order(Node.left)) 
    string += ' ' + str(Node.value) + ','
    string +=  str(self.__recursive_in_order(Node.right)) 
    return string

  def pre_order(self):
    if self.__root == None:
      return '[ ]'
    pre_order = self.__recursive_pre_order(self.__root)
    return '[' + pre_order[:-1] + ' ]'

  def __recursive_pre_order(self, Node):
    if Node == None:
      return ''
    string = ''
    string += ' ' + str(Node.value) + ','
    string += str(self.__recursive_pre_order(Node.left))
    string += str(self.__recursive_pre_order(Node.right))
    return string 

  def post_order(self):
    if self.__root == None:
      return '[ ]'
    post_order = self.__recursive_post_order(self.__root)
    return '[' + post_order[:-1] + ' ]'

  def __recursive_post_order(self, Node):
    if Node == None:
      return ''
    string = ''
    string += str(self.__recursive_post_order(Node.left))
    string += str(self.__recursive_post_order(Node.right))
    string += ' ' + str(Node.value) + ','
    return string 

  def to_list(self):
    to_list = []
    self.__recursive_to_list(self.__root, to_list)
    return to_list

  def __recursive_to_list(self, Node, list):
    if Node is None: 
      return
    self.__recursive_to_list(Node.left, list)
    list.append(Node.value)
    self.__recursive_to_list(Node.right, list)

  def get_height(self):
    if self.__height == 0 or self.__root == None:
      return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()
  
  def __compute_balance(self,t): 
    balance_factor = 0 
    if t.right == None and t.left == None: 
      balance_factor = 0
    elif t.right == None: 
      balance_factor = -1 * t.left.height
    elif t.left == None: 
      balance_factor = t.right.height 
    else: 
      balance_factor = t.right.height - t.left.height
    return balance_factor

  def __balance(self, t):   
    balance_factor = self.__compute_balance(t)   

    if balance_factor > 1 and self.__compute_balance(t.right) >= 0: 
      return self.__rotate_left(t) 
    
    elif balance_factor < -1 and self.__compute_balance(t.left) <= 0: 
      value = self.__rotate_right(t)
      return value
    
    elif balance_factor > 1 and self.__compute_balance(t.right) < 0: 
      t.right = self.__rotate_right(t.right)
      return self.__rotate_left(t)
    
    elif balance_factor < -1 and self.__compute_balance(t.left) > 0: 
      t.left = self.__rotate_left(t.left)
      return self.__rotate_right(t)
    
    else:
      return t

  def __rotate_left(self, t): 
    new_root = t.right
    t.right = new_root.left
    new_root.left = t
    self.__update_height(t) 
    self.__update_height(new_root)
    return new_root

  def __rotate_right(self,t):
    new_root = t.left
    t.left = new_root.right
    new_root.right = t
    self.__update_height(t)
    self.__update_height(new_root)
    return new_root

  def return_root(self):
    return self.__root.value

if __name__ == '__main__':
  new = Binary_Search_Tree()

  new.insert_element(60)
  new.insert_element(50)
  new.insert_element(70)
  new.insert_element(30)
  new.insert_element(55)
  new.insert_element(80)
  new.remove_element(60)
  new.remove_element(70)

  print('Root Node:', new.return_root())
  print('Height:', new.get_height())
  print('In Order:', new.in_order())
  print('Pre Order:', new.pre_order())
  print('Post Order:', new.post_order())
  print('To list:', new.to_list())
