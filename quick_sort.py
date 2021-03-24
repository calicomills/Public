################
###quick sort###
## Jishnu C K ##
################

import random



class Quicksort():

    count_comparisons = 0
    
    def quicksort(self,array_,l,r):
        
        if l >= r :
            return array_
        
        #print(l,r)
        #time.sleep(0.2)
 
        p = self.find_pivot(array_,l,r)
        #print(p)
        
        array_,np = self.partition(array_,l,r,p)
        #print(array_)

        self.quicksort(array_,l,np-1)

        self.quicksort(array_,np+1,r)

        return array_
        
    
    def partition(self,array_,l,r,p):
        
        self.count_comparisons += (r-l)
        pivot = array_[p]

        temp = array_[p]
        array_[p] = array_[l]
        array_[l] = temp
        #print (array_)
        i = l + 1
       
        for j in range(l+1,r+1):
            #print(j)
            if  array_[j] < pivot:
                temp = array_[j]
                array_[j] = array_[i]
                array_[i] = temp
                i+=1
            else:
                pass
            
        array_[l] = array_[i-1]
        array_[i-1] = pivot
            #print(pivot,array_)
        return array_,i-1


    def find_pivot(self,array_,l,r):
        #print(l,r)
        #return r
        m = int((l+r)/2)
        max_1 = l
        max_2 = r
        if array_[max_1] < array_[r]:
            max_2 = max_1
            max_1 = r
        if array_[max_1] < array_[m]:
            max_2 = max_1
            max_1 = m        
        elif array_[max_2] < array_[m]:
            max_2 = m



           
        
           
        #return max_2

        

           
        if l==r:
            return l
        return  random.randint(l, r)
       
        





arr = []
f = open("/Users/jishnu/calicomills_root/Public/data_2.txt","r")
for line in f.readlines():
    arr.append(int(line.split("\n")[0]))


#arr = [8,7,6,5,4,3,2,1,0]
obj = Quicksort()
sorted_ = obj.quicksort(arr,0,len(arr)-1)
print(obj.count_comparisons)

