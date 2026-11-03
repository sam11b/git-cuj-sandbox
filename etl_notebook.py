# Databricks notebook source
# MAGIC %md
# MAGIC # Daily sales ETL

# COMMAND ----------

# DBTITLE 1,Imports
from utils.cleaning import clean_sales
from pyspark.sql.functions import lit

# COMMAND ----------

# DBTITLE 1,Build and clean sales dataframe
df = spark.range(10).withColumnRenamed("id", "order_id")
df = df.withColumn("amount", lit(50))
df = clean_sales(df)
display(df)

# COMMAND ----------

THRESHOLD = 500
print(f"Threshold is {THRESHOLD}")