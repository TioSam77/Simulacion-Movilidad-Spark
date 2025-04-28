from pyspark.sql import SparkSession
from pyspark.sql.functions import hour, col
import matplotlib.pyplot as plt

def crear_spark_session():
    spark = SparkSession.builder \
        .appName("Analisis Movilidad CDMX - Bicis") \
        .getOrCreate()
    return spark

def leer_datos(spark, ruta_archivo):
    df = spark.read.csv(ruta_archivo, header=True, inferSchema=True)
    return df

def mostrar_informacion_basica(df):
    print("\n[Esquema de datos]")
    df.printSchema()

    print("\n[Muestra de datos]")
    df.show(10, truncate=False)

def analizar_hora_pico(df):
    print("\n[Viajes en hora pico (7-9 am y 5-7 pm)]")
    df_hora_pico = df.filter(
        (hour(col("hora_inicio")).between(7, 9)) |
        (hour(col("hora_inicio")).between(17, 19))
    )
    df_hora_pico.show()
    return df_hora_pico

def rutas_mas_congestionadas(df):
    print("\n[Rutas más populares]")
    rutas = df.groupBy("estacion_origen", "estacion_destino") \
              .count() \
              .orderBy("count", ascending=False)
    rutas.show()
    return rutas

def resumen_general(df):
    print("\n[Resumen general de viajes]")
    resumen_origen = df.groupBy("estacion_origen").count().orderBy("count", ascending=False)
    resumen_destino = df.groupBy("estacion_destino").count().orderBy("count", ascending=False)
    resumen_origen.show()
    resumen_destino.show()
    return resumen_origen, resumen_destino

def guardar_resultados_pandas(df, ruta_salida):
    pandas_df = df.toPandas()
    pandas_df.to_csv(ruta_salida, index=False)
    print(f"[Guardado CSV en: {ruta_salida}]")

def graficar_resumen_origenes(df):
    pandas_df = df.toPandas()

    plt.figure(figsize=(10, 6))
    plt.bar(pandas_df['estacion_origen'], pandas_df['count'], color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title('Cantidad de Viajes por Estación de Origen')
    plt.xlabel('Estación Origen')
    plt.ylabel('Cantidad de Viajes')
    plt.tight_layout()

    plt.savefig("grafica_origenes.png")
    print("[Gráfica guardada como 'grafica_origenes.png'].")

def main():
    spark = crear_spark_session()
    df = leer_datos(spark, "viajes_bici.csv")

    mostrar_informacion_basica(df)
    df_pico = analizar_hora_pico(df)

    rutas = rutas_mas_congestionadas(df_pico)
    resumen_origen, resumen_destino = resumen_general(df)

    guardar_resultados_pandas(rutas, "rutas_populares.csv")
    guardar_resultados_pandas(resumen_origen, "resumen_origenes.csv")
    guardar_resultados_pandas(resumen_destino, "resumen_destinos.csv")

    graficar_resumen_origenes(resumen_origen)
    
    spark.stop()

if __name__ == "__main__":
    main()