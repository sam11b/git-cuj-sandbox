# Databricks notebook source
# MAGIC %md
# MAGIC # Daily sales ETL

# COMMAND ----------

from utils.cleaning import clean_sales

# COMMAND ----------

df = spark.range(10).withColumnRenamed("id", "order_id")
df = clean_sales(df)
display(df)

# COMMAND ----------

THRESHOLD = 100
print(f"Threshold is {THRESHOLD}")
