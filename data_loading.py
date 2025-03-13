from pyspark.sql import SparkSession
spark = SparkSession.builder.\
         appName('spark project').getOrCreate()


def create_dataframe(data):
    df = spark.read.csv(data,header=True,inferSchema=True)
    return df
