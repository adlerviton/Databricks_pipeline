# Databricks notebook source
# MAGIC %python
# MAGIC from pyspark.sql.types import DoubleType, IntegerType, StringType, StructType, StructField
# MAGIC
# MAGIC # Define variables used in the code below
# MAGIC file_path = "/databricks-datasets/songs/data-001/"
# MAGIC table_name = "raw_song_data"
# MAGIC checkpoint_path = "/tmp/pipeline_get_started/_checkpoint/song_data"
# MAGIC
# MAGIC schema = StructType(
# MAGIC   [
# MAGIC     StructField("artist_id", StringType(), True),
# MAGIC     StructField("artist_lat", DoubleType(), True),
# MAGIC     StructField("artist_long", DoubleType(), True),
# MAGIC     StructField("artist_location", StringType(), True),
# MAGIC     StructField("artist_name", StringType(), True),
# MAGIC     StructField("duration", DoubleType(), True),
# MAGIC     StructField("end_of_fade_in", DoubleType(), True),
# MAGIC     StructField("key", IntegerType(), True),
# MAGIC     StructField("key_confidence", DoubleType(), True),
# MAGIC     StructField("loudness", DoubleType(), True),
# MAGIC     StructField("release", StringType(), True),
# MAGIC     StructField("song_hotnes", DoubleType(), True),
# MAGIC     StructField("song_id", StringType(), True),
# MAGIC     StructField("start_of_fade_out", DoubleType(), True),
# MAGIC     StructField("tempo", DoubleType(), True),
# MAGIC     StructField("time_signature", DoubleType(), True),
# MAGIC     StructField("time_signature_confidence", DoubleType(), True),
# MAGIC     StructField("title", StringType(), True),
# MAGIC     StructField("year", IntegerType(), True),
# MAGIC     StructField("partial_sequence", IntegerType(), True)
# MAGIC   ]
# MAGIC )
# MAGIC
# MAGIC (spark.readStream
# MAGIC   .format("cloudFiles")
# MAGIC   .schema(schema)
# MAGIC   .option("cloudFiles.format", "csv")
# MAGIC   .option("sep","\t")
# MAGIC   .load(file_path)
# MAGIC   .writeStream
# MAGIC   .option("checkpointLocation", checkpoint_path)
# MAGIC   .trigger(availableNow=True)
# MAGIC   .toTable(table_name)
# MAGIC )
