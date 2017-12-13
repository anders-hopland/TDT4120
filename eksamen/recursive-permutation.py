import copy
s = [2, 3, 4, 5, 6, 7, 8]

visited = []

def rec_func(set):
    if len(set) == 1:
        return

    temp_set = copy.deepcopy(set)
    for i in set:
        temp_set.pop(i)
        if temp_set not in visited:
            visited.append(temp_set)
            rec_func(temp_set)
            temp_set = copy.deepcopy(set)
        
rec_func(s)
print(visited)
