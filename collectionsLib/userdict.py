from collections import UserDict #wrapper around dictionary: create new dict from existing with modified or new functionality

class MyDict(UserDict):
    '''
        creating dict where deletion are not allowed
    '''
    
    def __del__(self):
        raise RuntimeError("__del__ method removed using UserDict functionality")
        
    def pop(self):
        raise RuntimeError("pop is not being supported: UserDict functionality")
        
    def popitem(self):
        raise RuntimeError("popitem is not being suppoted: UserDict functionality")    
        
student = MyDict({"name": "rohit", "age": 23})

student.pop("name")
    

