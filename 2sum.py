import sys
import threading


def main():

        arr = []
        f = open("/Users/jishnu/calicomills_root/Public/data_7.txt","r")
        for line in f.readlines():
            val = line.strip()
            arr.append(int(val))


        count = 0
        dic = {}

        for i in range(0,len(arr)):
                dic[arr[i]] = 1

        for t in range(-10000,10001):
            for i in range(0,len(arr)):
                if dic.get(t-arr[i],0) :
                    count = count + 1
                    break
        print count



if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
   
                
                