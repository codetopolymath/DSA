from collections import defaultdict

# default dict is used to initiate an empty dict [use to avoid keyValueError: key does not exists]

my_dict = defaultdict(list)

for i in range(10):
    my_dict[i].append(f"alpha:{i}".format(i))

print(my_dict)

