from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws


spark = SparkSession.builder.appName("Anonymize Data").getOrCreate()


df = spark.read.csv('/Volumes/project_codingquestion2/default/random_generated_csv/random_data.csv', header=True, inferSchema=True)


df = df.withColumn("first_name", sha2("first_name", 256)) \
       .withColumn("last_name", sha2("last_name", 256)) \
       .withColumn("address", sha2("address", 256))


df.write.csv('/Volumes/project_codingquestion2/default/anonymized_data/anonymized_data.csv', header=True)

display(df)

