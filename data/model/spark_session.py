import os
import sys
from pyspark.sql import SparkSession


os.environ['HADOOP_HOME'] = "C:/hadoop"
sys.path.append("C:/hadoop/bin")

spark = SparkSession.builder\
    .appName("pyspark_session")\
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3")\
    .getOrCreate()