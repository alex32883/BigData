from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 5)

lines = ssc.socketTextStream("localhost", 9999)

words = lines.flatMap(lambda line: line.split(" "))

pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

wordCounts.pprint()

ssc.start()
<<<<<<< HEAD
ssc.awaitTermination() 
=======
ssc.awaitTermination() 
>>>>>>> d9e1293b0836c44763880a220cfd1d5e915af917
