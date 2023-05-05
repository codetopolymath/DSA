from collections import ChainMap
# chainmap is used to combine multiple dict into one
#NOTE: make sure keys are not duplicated across dicts 

alphabets = {1: "a", 2: "b", 3: "c"}
numbers = {4:1, 5:2, 6:3}
capalphabets = {7: "A", 8: "B", 9: "C"}

chainmap_all = ChainMap(alphabets, numbers, capalphabets)

names = {10: "rohit", 11: "ghawale"}

chainmap_all = chainmap_all.new_child(names) # add new dict to existing chainmap

