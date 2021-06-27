#
'''
import sys

sys.setrecursionlimit(10**6)

f = open("/Users/jishnu/calicomills_root/Public/data_4.txt","r")

graph = {}
for line in f.readlines():
    if int(line.strip().split(" ")[0]) in graph.keys():
        graph[int(line.strip().split(" ")[0])].append(int(line.strip().split(" ")[1]))
    else:
        graph[int(line.strip().split(" ")[0])] = [int(line.strip().split(" ")[1])]

def reverse(G):
    new_G = {}
    for key in G:
        for j in range(len(G[key])):
                if G[key][j] not in new_G.keys():
                    new_G[G[key][j]] = [key]
                else:
                    new_G[G[key][j]].append(key)
    
    return new_G

key_list = [0]*list(graph.keys())[len(graph)-1]


def DFS(G):
    global key_list
    G_comp = []
    #leader = []
    #key_list[i-1] = 1
    
    if i in G.keys():
        for j in range(len(G[i])):
            if key_list[G[i][j]-1] != 1 :
                DFS(G,G[i][j])
    stack = [iter(range(len(G, 0, -1)))]
    
    
    stack = [iter(range(len(G), 0, -1))]
    while stack:
        try:
            child = next(stack[-1])
            if key_list[child-1] != 1:
                    key_list[child - 1] = 1

                # Do whatever you want to do in the visit
                    if child in G.keys():
                        stack.append(iter(G[child]))
                        
        except StopIteration:
            stack.pop()
            if child in G.keys():
                G_comp.append(child)
            
    return G_comp

def DFS_Loop(G,l):

    key_list = [0]*list(G.keys())[len(G)-1]
    scc = []
    ln = len(l)
    counter = 0
  

            
    stack = [iter(range(len(l),0,-1))]
    while stack:
        
        try:
            child = next(stack[-1])
            if key_list[child-1] != 1:
                    key_list[child - 1] = 1
                    counter+=1

                # Do whatever you want to do in the visit
                    if child in G.keys():
                        stack.append(iter(G[child]))
                        
        except StopIteration:
            stack.pop()
            scc.append(counter)
            counter = 0
            

            


    return scc
            
            
    
G = reverse(graph)
l = DFS(G)
key_list = [0]*list(graph.keys())[len(graph)-1]
scc = DFS_Loop(graph,l)
scc.sort(reverse=True)

#new = reverse(graph)
print(scc[0:6])
'''
def main():

    # make a graph and its reverse from the given data
    graph = {}
    graphR = {}
    f = open("/Users/jishnu/calicomills_root/Public/data_4.txt", 'r')
    line = f.readline()
    while line:
        edge = [int(e) for e in line.split()]
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graphR:
            graphR[edge[1]].append(edge[0])
        else:
            graphR[edge[1]] = [edge[0]]
        line = f.readline()

    # run depth-first search on graph reverse
    node_post = {}
    post_node = {}
    post = 1
    for node in graphR:
        if not (node in node_post):
            prev_dict, prev_index, prev_set = {}, 1, set([node])
            prev_dict[prev_index] = node
            try:
                nodes = graphR[node][:]
            except:
                nodes = []
            next_dict, next_index, next_set = {}, 0, set()
            for n in nodes:
                if not ((n in prev_set) or (n in next_set) or
                        (n in node_post)):
                    next_index += 1
                    next_dict[next_index] = n
                    next_set.add(n)
            while next_dict:
                if next_dict[next_index] in prev_set:
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                else:
                    prev_set.add(next_dict[next_index])
                    prev_index += 1
                    prev_dict[prev_index] = next_dict[next_index]
                    try:
                        nodes = graphR[next_dict[next_index]][:]
                    except:
                        nodes = []
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                    for n in nodes:
                        if not ((n in prev_set) or (n in next_set) or
                                (n in node_post)):
                            next_index += 1
                            next_dict[next_index] = n
                            next_set.add(n)
                    next_index = len(next_dict)
            post = post + len(prev_dict)
            for element in prev_dict:
                if not prev_dict[element] in node_post:
                    node_post[prev_dict[element]] = post - element
                    post_node[post - element] = prev_dict[element]

    # run DFS on graph (by reverse postorder)
    reverse_postorder = post_node.values()[::-1]
    marked = set()
    results = []
    order = 0
    lenght = len(reverse_postorder)
    while order < lenght:
        node = reverse_postorder[order]
        if (not (node in marked)):
            prev_dict, prev_index, prev_set = {}, 1, set([node])
            prev_dict[prev_index] = node
            try:
                nodes = graph[node][:]
            except:
                nodes = []
            next_dict, next_index, next_set = {}, 0, set()
            for n in nodes:
                if not ((n in prev_set) or (n in next_set) or (n in marked)):
                    next_index += 1
                    next_dict[next_index] = n
                    next_set.add(n)
            while next_dict:
                if next_dict[next_index] in prev_set:
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                else:
                    prev_set.add(next_dict[next_index])
                    prev_index += 1
                    prev_dict[prev_index] = next_dict[next_index]
                    try:
                        nodes = graph[next_dict[next_index]][:]
                    except:
                        nodes = []
                    next_set.remove(next_dict[next_index])
                    del next_dict[next_index]
                    next_index = len(next_dict)
                    for n in nodes:
                        if not ((n in prev_set) or (n in next_set) or
                                (n in marked)):
                            next_index += 1
                            next_dict[next_index] = n
                            next_set.add(n) 
                    next_index = len(next_dict)
            # add the size of the previous strongly connected component
            results.append(len(prev_dict))
        for element in prev_dict:
            marked.add(prev_dict[element])
        order += 1

    # output the sizes of the 5 largest SCCs in the given graph
    solution = ','.join(str(x) for x in sorted(results + [0] * 5,
                                               reverse=True)[:5])
    print solution


if __name__ == '__main__':
    main()
