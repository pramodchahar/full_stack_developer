class Vector:

    """Represents a multi dimenstional vector """

    def __init__(self,d):
        """Create d dimensional vector of zeros"""

        self._coordinates=[0]*d

    
    def __len__(self):
        """ Return the dimesnion of the vector """
        return len(self._coordinates)

    
    def __getitem__(self,j):
        """Return the value at particular coordinate"""
        return self._coordinates[j]

    def __setitem__(self,j,val):
        """Set jth coordinate to given value"""
        self._coordinates[j]=val

    def __add__(self,other_vec):
        """Return sum of two vectors"""
        if len(self._coordinates) !=len(other_vec):
            raise ValueError('Dimensions must be same ')
        result=Vector(len(other_vec))

        for i in range(len(other_vec)):
            result[i]=self[i]+other_vec[i]
        return result
    def __eq__(self,other):
        """Returns True if vector has same coordinate as other"""
        return self._coordinates== other._coordinates



my_vec=Vector(5)
print(my_vec.__len__())

my_vec[0]=1
my_vec[1]=8
my_vec[2]=-5
my_vec[3]=1
new_vec=[2,3,4,5,9]

res=my_vec + new_vec


print(res._coordinates)
