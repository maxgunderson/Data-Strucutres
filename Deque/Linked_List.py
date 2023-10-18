class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            self.val = val
            self.next = None 
            self.prev = None

    def __init__(self):
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__header.prev = None
        self.__trailer.next = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def append_element(self, val):
        new_node = self.__Node(val)

        self.__trailer.prev.next = new_node 
        new_node.prev = self.__trailer.prev 
        self.__trailer.prev = new_node 
        new_node.next = self.__trailer 

        self.__size += 1         

    def insert_element_at(self, val, index):    
        new_node = self.__Node(val)
        cur = self.__find(index)

        new_node.next = cur
        new_node.prev = cur.prev
        cur.prev.next = new_node
        cur.prev = new_node

        self.__size += 1
        
    def remove_element_at(self, index):
        cur = self.__find(index) 

        cur.prev.next = cur.next 
        cur.next.prev = cur.prev 

        self.__size -= 1 

        return cur.val 

    def get_element_at(self, index):
        cur = self.__find(index)
        return cur.val

    def rotate_left(self):
        if self.__size == 0 or self.__size == 1: 
            return 
        
        placeholder = self.remove_element_at(0) 
        self.append_element(placeholder) 

    def __str__(self):
        if self.__size == 0: 
            return '[ ]'
        else:
            list = [] 
            cur = self.__header.next 
            while cur is not self.__trailer: 
                list.append(str(cur.val)) 
                cur = cur.next 
            string = '[ ' + ', '.join(list) + ' ]' 
            return string 
        
    def __iter__(self):
        self.__cur = self.__header 
        return self 

    def __next__(self):
        if self.__cur.next == self.__trailer: 
            raise StopIteration
        self.__cur = self.__cur.next 
        return self.__cur.val
        
    def __reversed__(self):
        return_list = Linked_List() 
        if self.__size == 0: 
            return return_list
        else: 
            return_list.append_element(self.__trailer.prev.val) 
            cur = self.__trailer.prev.prev 
            while cur != self.__header: 
                return_list.append_element(cur.val) 
                cur = cur.prev 
            return return_list 

    def __find(self,index): 
        if index >= self.__size or index < 0: 
            raise IndexError('list index out of range')
        elif index <= (self.__size//2): 
            cur = self.__header.next 
            for i in range(0,index):
                cur = cur.next
            return cur
        elif index > (self.__size//2): 
            cur = self.__trailer.prev
            for i in range(self.__size,index+1,-1):
                cur = cur.prev
            return cur

if __name__ == '__main__':
  list = Linked_List()
  list.append_element(1)
  list.append_element("string")
  print(list)

