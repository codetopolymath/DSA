from collections import UserString


class MyString(UserString):

    def append(self, s):
        self.data += s
        
    def remove(self, s):
        self.data = self.data.replace(s, "")
        
        
my_string = MyString("rohit")
my_string.data
