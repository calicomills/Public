import re
import random

# Load the file into a graph represented by a dict of lists
def load_graph():
    g = {}

    f = open('/Users/jishnu/calicomills_root/Public/data_3.txt')
    lines = f.readlines()
    f.close()

    lines = map(lambda s: re.sub('\s+',' ',str(s.strip('\r\n'))).strip(),lines)
    lines = map(lambda s: s.split(' '),lines)

    for line in lines:
        g[int(line[0])] = map(lambda s: int(s),line[1:])
    
    return g

# Contract an edge between 2 vertices
def contract_edge(edge):
    global g 
    
    # merge v2 into v1 and remove v2 from graph
    v1l = g[edge[0]]
    v1l.extend(g[edge[1]])
    del g[edge[1]]
    
    #replace all occurnces of v2 value with v1
    for k, l in g.iteritems():
        g[k] = [edge[0] if x == edge[1] else x for x in g[k]]
    
    # Remove all edges of v1 to itself(loops)
    g[edge[0]] = [x for x in g[edge[0]] if x != edge[0]]
    
# Gets a random edge available in the current graph
def get_random_edge():
    v1 = random.randint(0,len(g)-1)
    v1 = list(g.keys())[v1]
    v2 = g[v1] [random.randint(0,len(g[v1])-1)]
    return (v1,v2)

minlist = []

# Repeat 10 times to get a minimum
for i in range(0,20):
    g = load_graph()

    # Keep contracting the graph until we have 2 vertices
    while(len(g) > 2):
        contract_edge(get_random_edge())
    
    minlist.append(len(list(g.keys())[0]))

print(min(minlist))