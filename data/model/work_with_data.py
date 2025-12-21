from pyspark.sql import DataFrame
from data.model.__init__ import *


Session = get_session()


def clean_data(df: DataFrame) -> DataFrame:
    pass

def correct_shem(df: DataFrame, table_name: str, url: str) -> bool:
    bd_df = spark.read.format('jdbc').option("url", url)\
        .option("dbtable", table_name)\
        .option("user", settings['pguser'])\
        .option("password", settings['password'])\
        .option("driver", "org.postgresql.Driver").load()
    return bd_df.schema == df.schema

def input_data(file_name: str) -> DataFrame:
    df = spark.read.format("csv") \
        .option("header", "True") \
        .option("inferSchema", "True") \
        .load(file_name)
    return df

def write_database(df: DataFrame, url_db: str, nametable: str) -> bool:
    try:
        if correct_shem(df, nametable, url_db):
            exist = spark.read.format('jdbc').option("url", url_db).option('dbtable', nametable).load()
            new_df = df.join(exist, on='ticker', how='left_anti')

            new_df.write.jdbc(
                url=url_db,
                table=nametable,
                mode="append",
                properties={
                    "user": settings['pguser'],
                    "password": settings['password'],
                    "driver": "org.postgresql.Driver",
                }
            )
            print("Данные успешно загружены")
        else:
            print("Схема не коректна")

    except Exception as e:
        print(e)
        print("Сбой при загрузке данных")
        return False

    else:
        return True