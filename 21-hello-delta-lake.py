# Databricks notebook source
spark.sql("USE CATALOG hive_metastore")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE product_info (
# MAGIC   product_id INT,
# MAGIC   product_name STRING,
# MAGIC   category STRING,
# MAGIC   price DOUBLE,
# MAGIC   quantity INT
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO product_info (product_id, product_name, category, price, quantity)
# MAGIC VALUES (1, 'Winter Jacket', 'Clothing', 79.95, 100);
# MAGIC INSERT INTO product_info (product_id, product_name, category, price, quantity)
# MAGIC VALUES
# MAGIC  (2, 'Microwave', 'Kitchen', 249.75, 30),
# MAGIC  (3, 'Board Game', 'Toys', 29.99, 75),
# MAGIC  (4, 'Smartcar', 'Electronics', 599.99, 50);

# COMMAND ----------

# MAGIC %sql
# MAGIC select category, price, quantity from product_info where quantity > 50;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL product_info

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/user/hive/warehouse/product_info/_delta_log

# COMMAND ----------

# MAGIC %fs
# MAGIC head dbfs:/user/hive/warehouse/product_info/_delta_log/00000000000000000000.json

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE product_info
# MAGIC SET price = price + 10
# MAGIC WHERE product_id = 3

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/user/hive/warehouse/product_info

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL product_info

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY product_info

# COMMAND ----------


