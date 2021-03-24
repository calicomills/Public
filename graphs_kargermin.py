import random

class Kargermin():
    def contraction_cut(self,node_):
        
        while(len(node_)>2):
     
            node_1 = list(node_.keys())[random.randint(0,len(node_)-1)]
            node_2 = node_[node_1][random.randint(0,len(node_[node_1])-1)]
            node_[node_1].extend(node_[node_2])
            if node_1 == node_2:#unlikely
                pass
            else:
                del node_[node_2]
                for key in node_:
                    for j in range(0,len(node_[key])):
                        if node_[key][j] == node_2:
                            node_[key][j] = node_1

                node_[node_1] = [x for x in node_[node_1] if x != node_1 ]

            
        return len(node_[list(node_.keys())[0]])

minlist = []
for i in range(0,40):
    arr = {}
    f = open("/Users/jishnu/calicomills_root/Public/data_3.txt","r")
    for line in f.readlines():
        arr[int(line.split("\t")[0])] = [int(i) for i in line.strip().split("\t")]
        
    minlist.append(Kargermin().contraction_cut(arr))

print(min(minlist))

