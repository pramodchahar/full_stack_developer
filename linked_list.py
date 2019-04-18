#implement data structure ( node class )
class node: 
    #create a constructor and pass an element (data point) to be stored by this node
    def __init__(self,data=None):
        #by default it would be set to None
        self.data=data
        #save the pointer to the next node
        self.next=None

#next we create a linked list class which basically is a wrapper which wraps node class we just created above ( user never going to interface with node class , this remains just a sub class of linked list)
class linked_list:
    def __init__(self):
        #declare the head node to make it always available inside the linked list
        #head node would actually not contain any actual data and nor going to be indexable ( In other words , user isnt going to be able to access this head node)
        #this is simply going to be used as a placeholder to allow us to point to the data element in the list 
        #head node is not a data node ( but it contains the pointer to the first data node )
        self.head=node()


    #create append function to lnked list class to create the first element of the list 
    def append(self,data):
        #create a new node of the class node and passing the data which will set the data element inside the node
        new_node=node(data)
        #now we create avariable to store the current node to ensure we are at the starting most node ( leftmost )
        cur=self.head
        #now we iterate over each of the nodes in the list and reach the node where next node is null , we can insert our new node 
        while cur.next !=None:
            #traverse through the list
            cur=cur.next
        #now that we are now at the last node , we can set the next node  to be the new node which we want to add 
        cur.next=new_node

    #create a function to figure out the length of the linked list

    def length(self):
        #create another variable to point to current node
        cur=self.head
        #create another variable to contain the total number of nodes we have seen
        total=0
        #begin iterating over nodes
        while cur.next != None:
            total+=1
            cur=cur.next
        return total

    #create a function to display contents of the linked list
    def display(self):
        #create list of elements seen
        elements=[]
        #set a new variable for current node we looking at
        cur=self.head

        # begin traversing over the nodes while next elemnt in node is not None
        while cur.next != None:
            cur=cur.next
            #append the data of the current node to the elements list
            elements.append(cur.data)
        return elements

    # define an extractor function to index data element from certain index

    def get(self,index):
        #put a check point to validate if index within the range 
        if index >= self.length():
            print("Index out of Range ")
            return None
        #set current index to 0 
        cur_idx=0
        #set the current node to starting node
        cur=self.head
        while True:
            #traverse over the entire nodes and set the current node to next node
            cur=cur.next
            # if index asked by user is current index , return the current node data 
            if cur_idx==index:
                return cur.data
            # else increase current index by 1 
            else:
                cur_idx+=1

    #define a function to delete the element at certain index 
    def erase(self,index):
        if index >= self.length():
            print("Index out of Range ")
            return None
        #set current index to 0
        cur_idx=0
        #set current node to starting node
        cur=self.head
        while True:
            #create the last node variable pointing to current node
            last_node=cur
            # move the cur node to next node
            cur=cur.next
            #check if index asked by user is same user , change the last node from pointing to current node to next node
            if cur_idx==index:
                last_node.next=cur.next
                return
            #increase the node by 1
            cur_idx+=1

            


            


my_list=linked_list()

my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)

print(my_list.length())
print(my_list.display())
print(my_list.get(3))
my_list.erase(2)
print(my_list.display())




