import threading
import sys

def TwoSum_HashTable(hashTable, lst, target):
    '''
    2-SUM algorithm via hash table.
    
    O(n) time.
    '''
    for x in lst:
        y = target-x
        if y in hashTable and x != y:
            return (x, y)
        
    return None
def main():
    
    lines = open('/Users/jishnu/calicomills_root/Public/data_7.txt').read().splitlines()
    #lines = open('2sum-tc/test1.txt').read().splitlines()
    data = map(lambda x: int(x), lines)

    #count = 0
    #for t in range(2500, 4000+1):
    #    if(TwoSum_Naive(data, t)):
    #        count += 1
    #print('Naive:' + str(count))
    
    #count = 0
    #sorted_data = sorted(data)
    #for t in range(2500, 4000+1):
    #    if(TwoSum_BinarySearch(sorted_data, t)):
    #        count += 1
    #print('Via binary search: ' + str(count))
    
    hashTable = dict()
    
    for x in data:
        hashTable[x] = True
    print('size:' + str(len(hashTable)))
        
    count = 0
    for t in range(-10000, 10000+1):
        #print "Round #" + str(t)
        if(TwoSum_HashTable(hashTable, data, t)):
            count += 1
            
    print('Via hash table: ' + str(count))
    

if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
    print "Running....."