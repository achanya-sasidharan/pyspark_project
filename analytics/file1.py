from pyspark.sql.functions import hour, count, concat_ws, col, lit, date_format
def peak_Hours(tablename):
    df = tablename.withColumn("hour", hour(col("order_time")))
    result = df.groupBy('hour').agg(count('order_id').alias('No_of_orders'))
    result = result.orderBy(result.No_of_orders.desc())


    result = result.withColumn("formatted_hour", concat_ws(":", col("hour"), lit("00")))
    result.show()
    df_with_12hr = result.withColumn("time_12hr", date_format(col("formatted_hour"), "hh:mm a"))
    return df_with_12hr


