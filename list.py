a=[]

class example:
    #constructor function with internal value of 10
    def __init__(self):
        self.value=10

# _ doesnt store value compared to i used in for loops
for _ in range(10):
    new_example=example()
    a.append(new_example)

print(a)

