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

THRESHOLD = 500
print(f"Threshold set to {THRESHOLD}")