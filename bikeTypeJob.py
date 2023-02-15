import os
from pyspark.sql import SparkSession

FILE_LOCATION = os.environ.get("FILE_LOCATION")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

spark = (SparkSession
         .builder
         .appName("rides-type-bikes")
         .getOrCreate())

spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", AWS_ACCESS_KEY_ID)
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", AWS_SECRET_KEY)

df = spark.read.csv("s3a://basan-bicycle/df_1_year.csv", header=True)
df.select("rideable_type").groupby("rideable_type").count().show()

spark.stop()