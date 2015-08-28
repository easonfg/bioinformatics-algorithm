import random
import copy
from collections import defaultdict, OrderedDict

inputs = open('rosalind_ba3e.txt', 'r').read().strip()
collection = inputs.split('\n')

print collection


text = open('sc.txt', 'a')
results = defaultdict(list)

#temp_col = copy.deepcopy(collection)

edges = defaultdict(list)
for pattern in collection:
    temp = pattern.split('->')
    #print 'TEMP' + str(temp)
    try:
        each = temp[1].split(',')
        #print map(int, each)
    except:
        continue
    edges[int(temp[0])] = map(int, each)

edges = dict(edges)
nodes = edges.keys()
#print nodes
#print edges

validation_edges = copy.deepcopy(edges)
start = random.choice(nodes)


while bool(validation_edges):
    # initial part
    validation_edges = copy.deepcopy(edges) # regenerate the edges in the beginning of loop
    path = []
    temp_candidate = []
    path.append(start) # path starts with start
    #print 'edges[path[-1]] is ' + str(path[-1]) + str(edges[path[-1]])
    next_node = random.choice(edges[path[-1]])
    #print next_node

    while next_node in validation_edges:     # while there are edges in the next node, then continue
        #print 'next_node is ' + str(next_node)
        path.append(next_node) # add the next node to the path
        #print path
        validation_edges[path[-2]].remove(next_node) # delete the edge between the next node and the node it came from

        if bool(validation_edges[path[-2]]) is False: # if there is no more edges from a node, delete the node from dictionary
            del validation_edges[path[-2]]
            #print 'removed' + str(path[-2])
            #print validation_edges
        else:
            #temp_dict[path[-1]] = copy.deepcopy(edges[path[-1]])
            temp_candidate.append(path[-2]) # if there are still nodes, add to temp candidate list, where a new start will be chosen

        next_node = random.choice(validation_edges[path[-1]]) # next node comes randomly from the last node on the path's edges
    else:
        del validation_edges[path[-1]]

    #print 'validation edges ' + str(validation_edges)
    #print 'CANDIDATE' + str(temp_candidate)
    #print 'CANDIDATE' + str(temp_candidate)
    start = random.choice(temp_candidate)
    temp_candidate.remove(start)
else:
    path.append(path[0])
    print path

#print results
#for key, val in results.items():
#    #print key, str(val)
#    inputting =  key + ' -> ' + (','.join(val)) + '\n'
#    text.write(inputting)

#    temp_col.remove(pattern)
#    for remainder in temp_col:
#        #print pattern, remainder
#        #import pdb
#        #pdb.set_trace()
#        if pattern[0:-1] == remainder[1:]:
#            results.append(remainder + ' -> ' + pattern)
#        if pattern[1:] == remainder[0:-1]:
#            results.append(pattern + ' -> ' + remainder)
#            #print (pattern + '->' + remainder)
#            #text.write('yay')
#            #text.write(pattern + '->' + remainder)

#text.write('\n'.join((results)))
