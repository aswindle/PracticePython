def remove_dupes(my_list):
    new = []
    for i in range(0, len(my_list)):
        if my_list[i] not in new:
            new.append(my_list[i])

    return new

def remove_dupes_set(my_list):
    new = set(my_list)
    return new
    
a = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'f']
print(remove_dupes(a))
print(remove_dupes_set(a))