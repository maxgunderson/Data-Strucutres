from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__size = 0
    self.__front_Index = 0
    self.__back_Index = 0

  def __str__(self):
    if self.__size == 0:
      return '[ ]' 
    else: 
      list = [] 
      for i in range(0, self.__size): 
        list.append(str(self.__contents[(i + self.__front_Index + self.__capacity) % self.__capacity])) 
      string = '[ ' + ', '.join(list) + ' ]' 
      return string
    
  def __len__(self):
    return self.__size

  def __grow(self):
    self.__capacity = self.__capacity * 2 
    new_arr = [None] * self.__capacity 
    
    for i in range(0, self.__size): 
      new_arr[i] = self.__contents[(i + self.__front_Index) % self.__size]
  
    self.__front_Index = 0 
    self.__back_Index = self.__size - 1 

    self.__contents = new_arr

  def push_front(self, val):
    if self.__size == 0: 
      self.__contents[self.__front_Index] = val

    elif self.__size == self.__capacity: 
      self.__grow()
      self.__front_Index = (self.__front_Index + self.__capacity - 1) % self.__capacity 
      self.__contents[self.__front_Index] = val 

    else: 
      self.__front_Index = (self.__front_Index - 1 + self.__capacity) % self.__capacity 
      self.__contents[self.__front_Index] = val 

    self.__size += 1
    
  def pop_front(self):
    if self.__size == 0: 
      return 
    else:
      return_val = self.__contents[self.__front_Index]
      self.__front_Index = (self.__front_Index + self.__capacity + 1) % self.__capacity
      self.__size -= 1
      if self.__size == 0:
        self.__front_Index = self.__back_Index
      return return_val

  def peek_front(self):
    if self.__size == 0:
      return 
    return self.__contents[self.__front_Index]
    
  def push_back(self, val):
    if self.__size == 0:
      self.__contents[self.__back_Index] = val
    
    elif self.__size == self.__capacity:
      self.__grow()
      self.__back_Index = (self.__back_Index + self.__capacity + 1) % self.__capacity
      self.__contents[self.__back_Index] = val

    else:
      self.__back_Index = (self.__back_Index + self.__capacity + 1) % self.__capacity
      self.__contents[self.__back_Index] = val
    
    self.__size += 1
  
  def pop_back(self):
    if self.__size == 0:
      return 
    else: 
      return_val = self.__contents[self.__back_Index]
      self.__back_Index = (self.__back_Index + self.__capacity - 1) % self.__capacity
      self.__size -= 1
      if self.__size == 0:
        self.__back_Index = self.__front_Index
      return return_val

  def peek_back(self):
    if self.__size == 0:
      return
    return self.__contents[self.__back_Index]
