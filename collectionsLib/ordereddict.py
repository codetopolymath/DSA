from collections import OrderedDict

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

ordered_dict = OrderedDict(my_dict) # create array of tuple `OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])`

normal_dict = dict(my_dict) # create normal dict `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`
