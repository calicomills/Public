################
###Finding inversions in an unsorted array while sorting###
## Jishnu C K ##
################


class Find_invs():
    
    def count(self,array_):
        l = len(array_)
        if l == 1:
            return array_,0
        m = l/2 - 1
        left = [0]* (l/2)
        right = [0]* (l - l/2)
        i = 0
        j = 0
        for k in range(l):
            if k <= m:
                left[i] = array_[k]
                i+=1
            else:
                right[j] = array_[k]
                j+=1
  
        left,x = self.count(left)
        right,y = self.count(right)
        c,z = self.count_split(left,right)

        return c,(x + y + z)

    def count_split(self,left,right):
        i = 0
        j = 0
        c = [0]*(len(left) + len(right))
        len_left = len(left)
        counter_n = 0
        for k in range(0,len(left) + len(right)):
            
           
            
            if i >= len(left):
                c[k] = right[j]
                j+=1
                #counter_n+=len_left
                
            elif j >= len(right):
                c[k] = left[i]
                #len_left-=1
                i+=1

            elif(left[i] < right[j]):
                c[k] = left[i]
                len_left-=1
                i+=1
                
            else :
                c[k] = right[j]
                j+=1
                counter_n+=len_left
        
        return c,counter_n
arr = []
f = open("/Users/jishnu/calicomills_root/Public/data.txt","r")
for line in f.readlines():
    arr.append(int(line.split("\n")[0]))


#arr = [1,2,3,4,3,2,6,8,7,9,8,9,8,8,9]
obj = Find_invs()
obj.count(arr)
sorted_,inv_count = obj.count(arr)
print(inv_count)

