import pandas as pd
from snowflake.connector import connect

def load_to_csv(df, output_file):
    """
    Guarda el DataFrame transformado en CSV local
    """
    df.to_csv(output_file, index=False)
    print(f"Datos cargados en {output_file}")

def load_to_snowflake(df, user, password, account, warehouse, database, schema, table):
    """
    Carga un DataFrame a Snowflake
    """
    conn = connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )
    
    success, nchunks, nrows, _ = df.to_sql(
        table,
        con=conn,
        index=False,
        if_exists='append',  # o 'replace' según necesidad
        method='multi'
    )
    
    print(f"{nrows} filas cargadas a Snowflake en la tabla {table}")
    conn.close()

if __name__ == "__main__":
    df = pd.read_csv("processed/data_transformed.csv")
    load_to_csv(df, "processed/data_final.csv")
