#Binary tree implementation

class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree():
    def __init__(self,):
        self.root=None

    
    #insert function
    def insert(self,value):
        #if there is no root value
        if self.root==None:
            #assign the first value to root by using node class 
            self.root=node(value)
        else:
            #use private function 
            self._insert(value,self.root)

    
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            

#added nothing 
