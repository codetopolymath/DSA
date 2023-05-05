from collections import UserList #wrapper around list objects [list with modified or  additional functionality]

class MyList(UserList):
    
    def remove(self, s=None):
        raise RuntimeError("remove operation blocked")
        
    def pop(self, s=None):
        raise RuntimeError("pop method blocked")
        
my_list = MyList([1,2,3,4,5])

my_list.pop() #





