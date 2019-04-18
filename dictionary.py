#use class as dictionary object

class dict_obj():
    def __init__(self):
        self.data='data'

#create instance of the class
my_instance=dict_obj()

new_dict={}

new_dict['object']=my_instance
print(new_dict['object'].data)

print(new_dict.items())

# To iterate over key,value pairs in dictionary

for key,value in new_dict.items():
    print(key,value)

# DICT Vs LIST 


class_names=['ziaan','pramod','neha','hazard','neo','walmart','google','now','2019']

def create_dataset():
    import random
    num_entries=50000
    f=open("data.txt","w")
    for i in range(num_entries):
        current=random.choice(class_names)
        f.write(current+"\n")

    f.close()


def read_data_using_list():
    #create another list to save the frequency count of same size and initiate with 0 values
    name_counts=[]
    for name in class_names:
        name_counts.append(0)
    with open("data.txt","r") as f:
        #iterate over each row
        for line in f:
            line=line.strip()
            #till you reach the last row
            if line!=" ":
                #find the index value of current row name from original class names list and increase the count for that index
                name_counts[class_names.index(line)]+=1
    print(name_counts)


def read_data_using_dict():
    name_dict={}
    for name in class_names:
        name_dict[name]=0
    with open("data.txt","r") as f:
    #iterate over each row
        for line in f:
            line=line.strip()
            #till you reach the last row
            if line!=" ":
                name_dict[line]+=1
    print(name_dict)


import time

# t0=time.time()
# create_dataset()
# t1=time.time()
# #f'{value:{width}.{precision}}'
# print('Time taken to create dataset %0.1f second')%(t1-t0)


t2=time.time()
create_dataset()
t3=time.time()
#f'{value:{width}.{precision}}'
print('Time taken to read dataset using list  %0.5f second')%(t3-t2)

t4=time.time()
read_data_using_dict()
t5=time.time()
#f'{value:{width}.{precision}}'
print('Time taken to read dataset using dict %0.5f second')%(t5-t4)




