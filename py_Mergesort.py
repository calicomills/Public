################
###Merge Sort###
## Jishnu C K ##
################
class Mergesort():
    def mergesort(self,array_):
        l = len(array_)
        if l <= 1:
            return array_
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
            
        left = self.mergesort(left)
        right = self.mergesort(right)
        return self.merge(left,right)

    def merge(self,left,right):
        print("called merge")
        print(left,right)
        i = 0
        j = 0
        c = [0]*(len(left) + len(right))

        for k in range(0,len(left) + len(right)):
            
            if i >= len(left):
                c[k] = right[j]
                j+=1
                
            elif j >= len(right):
                c[k] = left[i]
                i+=1

            elif(left[i] < right[j]):
                c[k] = left[i]
                i+=1
                
            else :
                c[k] = right[j]
                print(c[k])
                j+=1

        return c

