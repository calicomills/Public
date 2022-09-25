from pyspark.sql import SparkSession
# Start spark session
spark = SparkSession.builder.appName('PySpark').getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize(["b", "a", "c"])
rdd.map(lambda x: (x, 1))

rdd = sc.parallelize(["b", "a", "c"])
sorted(rdd.map(lambda x: (x, 1)).collect())

print(rdd)

sc.parallelize([2, 3, 4, 5, 6]).cache().take(2)
sc.parallelize(range(100)).filter(lambda x: x > 90).take(3) #take()

sc.parallelize(range(100)).filter(lambda x: x > 90).take(3) #take()
sc.parallelize([3,4,5]).map(lambda x: [x,  x*x]).collect()

rdd = sc.parallelize([1, 2, 3, 4, 5])
# Collect is expensive in real time as it sends the data from all executers to spark master.
rdd.filter(lambda x: x % 2 == 0).collect() # Return a new RDD containing only the elements that satisfy a predicate. 

x = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
x.groupByKey().map(lambda x : (x[0], list(x[1]))).collect() 


x = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
x.groupByKey().map(lambda x : (x[0], list(x[1]))).collect() 


from operator import add
rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1)])
sorted(rdd.reduceByKey(add).collect())


wordsList = ['cat', 'elephant', 'rat', 'rat', 'cat']

wordsRDD = sc.parallelize(wordsList, 4) # number of partitions - 4

print(wordsRDD.collect())

itemsRDD = wordsRDD.mapPartitions(lambda iterator: [','.join(iterator)])
# mapPartitions() loops through 4 partitions and combines('rat,cat') in 4th iteration.
print (itemsRDD.collect())

L = range(1,10)

parallel = sc.parallelize(L, 3) # number of partitions - 3

def f(iterator): 
  yield sum(iterator)


parallel.mapPartitions(f).collect()

rdd = sc.parallelize([1, 2, 3, 4], 2) # number of partitions - 2

def f(iterator):
  yield sum(iterator)

rdd.mapPartitions(f).collect() 



#mapPartitionsWithIndex
x = sc.parallelize([1,2,3,4,5,6,7,8,9],2)
def f(partitionIndex,iterator): yield (partitionIndex,sum(iterator)) 
y = x.mapPartitionsWithIndex(f)
#glom() flattens elements on the same partitions
print(x.glom().collect())
print(y.glom().collect())





def f(inputRDD):
  return inputRDD
def add(A, B):
  return A + str(B)
sorted(inputRDD.combineByKey(str, add, add).collect())
































