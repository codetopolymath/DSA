from collections import deque # deque: double ended queue
#NOTE: deque are used when quick append and remove operation needed at both end on container[hold objects]

'''
normal deque allow insersion and deletion on both end, but
based on action: type of restricted deque

    Input Restricted Deque:
        input limited to one end while deletion is allowed on both
        
    Output Restricted Deque:
        output limited to one end while insersion is allowed on both
'''

student = deque(["name", "age", "field"]) #defining deque

student.append(["rohit", 23, "chemical"]) # appends on right end on deque
student.appendleft(["ghawale", 23, "engineering"]) # appends on left end of deque

student.pop() # deletion on right end
student.popleft() # deletion on leftend
