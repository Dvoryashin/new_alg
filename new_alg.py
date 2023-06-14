import time
graph = {}

graph['a'] = ['c', 'e']
graph['c'] = ['d']
graph['d'] = ['b']
graph['e'] = ['b', 'k', 'i']
graph['k'] = ['c', 'd']
graph['i'] = ['l']
graph['l'] = ['f']
graph['f'] = ['b']

paths = {}

def cheapest_path(graph, paths, start, end):

    arr = []

    if end in graph[start]:
        arr.append(start)
        return arr

    for parent, child in graph.items():

        for item in child:
            # айтемы, которые имеют соседей
            if graph.get(item):

                if end in graph[item]:

                    arr.append(parent + item)
                
                for item2 in graph[item]:

                    if graph.get(item2):

                        if end in graph[item2]:

                            arr.append(parent + item + item2)
    return arr

arr = cheapest_path(graph, paths, 'a', 'b')

print(arr)
null_and_own = []
end_arr = []

for i in range(0, len(arr)):
    if arr[i][0] != 'a':
        past = ''.join(arr[i])
        arr[i] = ''.join(cheapest_path(graph, paths, 'a', arr[i][0]))
        arr[i] = arr[i] + past
        
for i in range(0, len(arr)):
    arr[i] = arr[i] + 'b'
print(set(arr))




