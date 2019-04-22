def square_num(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result

print(square_num([1,2,3,4,5]))

#generators dont hold the entire result in the memory , it yeilds one result at a time
def square_generator(nums):
    for i in nums:
        yield (i*i)

my_num=square_generator([1,2,3,4,5])
# print(next(my_num))
# print(next(my_num))
# print(next(my_num))
# print(next(my_num))
# # print(next(my_num))

# for num in my_num:
#     print(num)

print(list(my_num))


# generator Vs list ( Generator is better in performance as it doesnt hold values in memory)

import memory_profiler as mem_profile
import random
import time

names=['john','hazard','ziaan','neha','pramod','test']
majors=['history','geo','maths','physics','hindi','politics']

print(f'The memory before : {mem_profile.memory_usage()} Mb')

#list function 

def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
            'id':i,
            'name': random.choice(names),
            'majors':random.choice(majors)

        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name': random.choice(names),
            'majors':random.choice(majors)

        }
        yield person

t1=time.process_time()
people=people_list(1000000)
t2=time.process_time()

print(f'The memory after operation  : {mem_profile.memory_usage()} Mb')

print(f'The total time taken : {t2-t1} seconds ')


t3=time.process_time()
people_gen=people_generator(1000000)
t4=time.process_time()

print(f'The memory after operation  : {mem_profile.memory_usage()} Mb')

print(f'The total time taken : {t4-t3} seconds ')





