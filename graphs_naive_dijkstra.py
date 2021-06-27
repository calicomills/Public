arr = {}
f = open("/Users/jishnu/calicomills_root/Public/data_5.txt","r")
for line in f.readlines():
        arr[int(line.split("\t")[0])] = [i.split(",") for i in line.strip().split("\t")[1:]]
X = []
A = [100000] * (len(arr)+1)
s = 1
A[s] = 0

while len(X) < 200:
    for j in range(0,len(arr[s])):
        if int(arr[s][j][0]) not in X:
            A[int(arr[s][j][0])] = min(A[s] + int(arr[s][j][1]),A[int(arr[s][j][0])])

    X.append(s)
    min_val = 100000
    for i in range(1,len(A)):
        if i not in X and A[i] < min_val:
            min_val = A[i]
            min_s = i
    s = min_s
    print s
      
for i in [7,37,59,82,99,115,133,165,188,197]:
    print str(A[i])+",",

        